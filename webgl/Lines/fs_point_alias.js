var fs_point_alias = `
precision mediump float;
varying  vec4 color;
 
void
main()
{
    float r = 0.0, delta = 0.01, alpha = 1.0;
	// y = mx + c
	r = gl_PointCoord.t * 0.5;
	if((gl_PointCoord.s > (r+delta)) || (gl_PointCoord.s < (r-delta)) )
		discard;
	

    gl_FragColor = color * (alpha);
}`;