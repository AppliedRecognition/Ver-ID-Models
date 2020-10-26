
Davis King resnet model with final offset to center the vectors.

The -rgb- models have standard rgb input layer offset.

The -norm- models have an additional mean and standard deviation input normalization layer.

The float32 and bfloat16 models result in floating point calculation.

Quantized models at q08 and below result in 8-bit fixed point calculation on mobile (ARM) platforms.
This is the fastest calculation method.

On x86 all quantized models use 16-bit calculation.

The q04 models definately suffer reduced accuracy.
The q16 models might suffer from reduced accuracy due to input data quantization.

