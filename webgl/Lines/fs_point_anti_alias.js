var fs_point_anti_alias = `
#ifdef GL_OES_standard_derivatives
#extension GL_OES_standard_derivatives : enable
#endif

precision mediump float;
varying  vec4 color;
 
void main()
{
    float r = 0.0, delta = 0.0, alpha = 1.0;
	
		// y = mx + c
	r = gl_PointCoord.t * 0.5;

	
	
    //vec2 cxy = 2.0 * gl_PointCoord - 1.0;
    //r = dot(cxy, cxy);
#ifdef GL_OES_standard_derivatives
    delta = fwidth(r);
    alpha = 1.0 - smoothstep(1.0 - delta, 1.0 + delta, r);
#endif

	if((gl_PointCoord.s > (r+delta)) || (gl_PointCoord.s < (r-delta)) )
		discard;
	
gl_FragColor = color * alpha;

}`;