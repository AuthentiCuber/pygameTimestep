# pygameTimestep

Implements a decoupled update and rendering to make any code framerate independant.  
Based on Gafferongames ["fix your timestep"](https://gafferongames.com/post/fix_your_timestep/#the-final-touch).

## Requirements
- Python 3.8+
- Pygame-ce 2.4+

## Why?
Multiplying everything by deltatime is annoying and sometimes doesn't work