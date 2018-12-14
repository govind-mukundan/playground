#!/usr/bin/env node

var amqp = require('amqplib');

const BROKER_ADDRESS = 'amqp://xxx.amazonaws.com'
const DEFAULT_EXCHANGE_NAME = 'com.xyz'

var args = process.argv.slice(2);
var key = (args.length > 0) ? args[0] : 'info';
var message = '{"topic":"blah", "msg":"hello world"}'; //args.slice(1).join(' ') || 'Hello World!';

amqp.connect(BROKER_ADDRESS).then(function(conn) {
  return conn.createChannel().then(function(ch) {
    var ex = DEFAULT_EXCHANGE_NAME;
    var ok = ch.assertExchange(ex, 'topic', {durable: false});
    return ok.then(function() {
      ch.publish(ex, key, Buffer.from(message));
      console.log(" [x] Sent %s:'%s'", key, message);
      return ch.close();
    });
  }).finally(function() { conn.close(); })
}).catch(console.log);