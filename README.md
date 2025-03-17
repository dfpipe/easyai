
# EazyAI

EazyAI is a simple Python library that enables developers to easily integrate advanced AI models into their applications without worrying about model infrastructure, training, or hosting.

Check out the [Dfpipe.EazyAI](https://dfpipe.com) for more information.

## Features

- Simple API for AI-related tasks
- Pre-configured access to powerful AI models
- No need to manage model infrastructure
- Easy integration with existing Python applications

## Installation

```bash
# clone the repo
git clone https://github.com/dfpipe/eazyai.git
cd eazyai

# install the package
pip install -e .
```

## Examples

### Run the streamlit demo

```bash
cd streamlit-demo && bash run.sh
```

### Use the Logo Detection model

```python
from eazyai.logo import EazyaiLogoV4, draw_bounding_boxes
from eazyai.utils import smart_read_image_v1

model = EazyaiLogoV4()
image = smart_read_image_v1('images/pexels-photo-29252132.webp')
result = model.detect_image(image)
# get 1st image's result
result = result[0]
image = draw_bounding_boxes(image, result['prediction_list'])
```



