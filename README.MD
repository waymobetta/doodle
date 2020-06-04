doodle

### what
- reads randomly ordered entries from [zettlekasten](https://zettelkasten.de/) back to the user.

### why
- continuously storing one's thoughts through a [zettlekasten](https://zettelkasten.de/) serves as a minor memory download so as to not bear burder of holding on to many interconnected thoughts.
- this also grants the privilege of introspection and reflection on concepts, allowing the iterative design and improvement process to begin more readily and with a proper environment to grow infinitely.
- moreover, by continuously being fed one's own thoughts, new linkages and concepts may be derived more effortlessly.

### steps

1. `git clone https://github.com/waymobetta/doodle.git`
2. download [jrnl](https://github.com/jrnl-org/jrnl)
3. configure [doodle_config.py](https://github.com/waymobetta/doodle/blob/master/src/doodle_config.py)
4. run [create_jrnl.py](https://github.com/waymobetta/doodle/blob/master/src/create_jrnl.py) to create a new custom jrnl
5. run [funnel.py](https://github.com/waymobetta/doodle/blob/master/src/funnel.py) helper script (or set cron)
6. run [doodle.py](https://github.com/waymobetta/doodle/blob/master/src/doodle.py) on a newly written jrnl

### todo
- [x] proof of concept
- [] read entry across all custom journals; display origin
- [] error handling
- [] integrate AI model for text generation

### sources
- [jrnl](https://github.com/jrnl-org/jrnl)

