```python
from cringelog import logger, Colors

logger.path = "logs.log"
logger.debug("this is debug message")


logger.setColor('DEBUG', color=Colors.BLACK)
logger.debug("debug again")
```
