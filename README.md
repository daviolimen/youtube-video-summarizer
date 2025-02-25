# Youtube Video Summarizer

This is a python-based program to sum up youtube videos using youtube transcript api and google generative ai libraries.

## Getting Started

First of all, clone the repository to your local machine.
```bash
git clone https://github.com/daviolimen/youtube-video-summarizer.git
```

### Prerequisites

Create a virtual environment of your preference and install the requirements from the requirements.txt file.

```
pip install -r requirements.txt
```

### Setting up your own API key

As said before, this project utilizes the google generative ai. In order for it to run, you must get your own google api key, this can be done at [Create API key](https://aistudio.google.com/app/apikey). After that, you just need to run main.py and select 1 to set up your API key, it will be stored in the file api_key.txt

### Running

Now you should be good to go, you just need to select 2 to sum up the video and input its link.

After the function is done running, the summary of the video will be on the response.md file.

Obs: When asked to input the youtube link, use the standard youtube link that you find in the browser's search bar, with the parameter "v=".

That's all, you may now enjoy the youtube video summarizer.