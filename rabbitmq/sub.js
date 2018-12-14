#!/usr/bin/env node

var amqp = require('amqplib');
var basename = require('path').basename;
var all = require('bluebird').all;
const BROKER_ADDRESS = 'amqp://xxx.amazonaws.com'

var keys = process.argv.slice(2);
if (keys.length < 1) {
  console.log('Usage: %s pattern [pattern...]',
              basename(process.argv[1]));
  process.exit(1);
}

amqp.connect(BROKER_ADDRESS).then(function(conn) {
  process.once('SIGINT', function() { conn.close(); });
  return conn.createChannel().then(function(ch) {
    var ex = 'topic_logs';
    var ok = ch.assertExchange(ex, 'topic', {durable: false});

    ok = ok.then(function() {
      return ch.assertQueue('', {exclusive: true});
    });

    ok = ok.then(function(qok) {
      var queue = qok.queue;
      return all(keys.map(function(rk) {
        console.log("binding to queue " + queue + " with routing key " + rk);
        ch.bindQueue(queue, ex, rk);
      })).then(function() { return queue; });
    });

    ok = ok.then(function(queue) {
      return ch.consume(queue, logMessage, {noAck: true});
    });
    return ok.then(function() {
      console.log(' [*] Waiting for logs. To exit press CTRL+C.');
    });

    function logMessage(msg) {
      console.log(" [x] %s:'%s'",
                  msg.fields.routingKey,
                  msg.content.toString());
    }
  });
}).catch(console.warn);