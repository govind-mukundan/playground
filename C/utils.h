/*
 * utils.h
 *
 *  Created on: 2 Apr 2018
 *      Author: gvm
 */

#ifndef INC_UTILS_H_
#define INC_UTILS_H_

/************************************************************************/
/* DEBUG                                                    */
/************************************************************************/

#ifndef DPRINTF_INFO
#define KNRM  "\x1B[0m"
#define KRED  "\x1B[31m"
#define KGRN  "\x1B[32m"
#define KYEL  "\x1B[33m"
#define KBLU  "\x1B[34m"
#define KMAG  "\x1B[35m"
#define KCYN  "\x1B[36m"
#define KWHT  "\x1B[37m"
#define CLRSCR "\033[2J"
// The \n causes printf() to flush
#define DPRINTF_ERROR(fmt, ...)         do { printf("%s [%s],[%d]", KRED, __FUNCTION__, __LINE__); printf(fmt, ##__VA_ARGS__); printf("%s\n", KNRM); } while(0);
#define DPRINTF_WARN(fmt, ...)          do { printf("%s", KYEL); printf(fmt, ##__VA_ARGS__); printf("%s\n", KNRM); } while(0);
#define DPRINTF_INFO(fmt, ...)          do { printf("%s", KGRN); printf(fmt, ##__VA_ARGS__); printf("%s\n", KNRM); } while(0);
#endif


/************************************************************************/
/* Some Useful MACROS                                                   */
/************************************************************************/
// Stringify a macro parameter
#define STR_HELPER(x) #x
#define STR(x) STR_HELPER(x)

// align pointer to x bytes boundary
#define align(ptr, bytes) \
((typeof(ptr))(((uintptr_t)(ptr) + (bytes)-1) & ~((bytes)-1)))


// check is pointer is memory aligned to x bytes
#define isaligned(ptr, bytes) \
(((uintptr_t)(ptr) & ((bytes)-1)) == 0)

// size of variable without sizeof operator
// size_t is unsigned int
#define size(var) \
((size_t)(&(var)+1) - (size_t)(&(var)))

// size of type without sizeof operator
#define sizetype(type) \
((size_t)(((type *)0) + 1)

// find if integer is power of 2
// power of two means only one bit is set.
#define power2(x) \
(x != 0 && (x & (x-1) == 0)))

#define IsNULL(x)		(((x) == (NULL)))
#define IsNotNULL(x)	(!IsNULL(x))
#define IS_ALIGNED(x, a)            (((x) & ((typeof(x))(a) - 1)) == 0)
#define ARRAY_SIZE(arr)				(sizeof(arr) / sizeof((arr)[0]))
// Find the sizeof struct element
#define Z_SIZEOF(type, member)          sizeof(((type *)0)->member)

#define roundup(x, y) (                                 \
{                                                       \
	const typeof(y) __y = y;							\
	(((x) + (__y - 1)) / __y) * __y;					\
}                                                       \
)
#define rounddown(x, y) (                               \
{                                                       \
	typeof(x) __x = (x);								\
	__x - (__x % (y));									\
}                                                       \
)


// Given a Little Endian byte stream, convert to:
#define Z_MAKEU32(p)            ((uint32_t)(*((uint8_t*)p+0) << 0) | (uint32_t)(*((uint8_t*)p+1) << 8) | (uint32_t)(*((uint8_t*)p+2) << 16) | (uint32_t)(*((uint8_t*)p+3) << 24))
#define Z_MAKEU16(p)            ((uint32_t)(*((uint8_t*)p+0) << 0) | (uint32_t)(*((uint8_t*)p+1) << 8))

#define Z_BitClear(val, mask)			((val) = (val) & (~(mask)))
#define Z_BitSet(val, mask)				((val) = (val) | (mask))
#define Z_BitIsSet(val, mask)           (((val) & (mask)) == (mask))
#define Z_BitIsClear(val, mask) 		(!(((val) & (mask)) == (mask)))

#endif /* INC_UTILS_H_ */
