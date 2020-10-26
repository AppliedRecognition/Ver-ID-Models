
Facenet model with 128 element output normalized for cosine similarity.

The float32 and bfloat16 models result in floating point calculation.

Quantized models at q08 and below result in 8-bit fixed point calculation on mobile (ARM) platforms.
This is the fastest calculation method.

On x86 all quantized models use 16-bit calculation.

Only at q04 is accuracy significantly reduced.

The q06 model is the recommended model for small size and speed without any noticable accuracy loss.

The q16 model might suffer from reduced accuracy due to input data quantization.

