from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import google.generativeai as genai

def get_api_key():
    api_key = ''
    with open('api_key.txt', 'r') as api_file:
        api_key = api_file.read(100)
    return api_key

def get_video_id():
    video_link = input("What is the link of the youtube video you want to sum up?\nPlease use the standard video URL, with the \"v=\" parameter\n")
    
    video_link_equals_sign = video_link.find('=')

    if (video_link_equals_sign == -1):
        print("Sorry, the provided URL does not seem right.")
        return
    
    video_id = video_link[video_link_equals_sign + 1 :]

    return video_id

def get_transcripted_text(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    formatter = TextFormatter()

    txt_formatted = formatter.format_transcript(transcript)

    return txt_formatted

def get_video_summary(transcripted_text, api_key):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel()

    try:
        response = model.generate_content(f"Could you sum up the following video for me? The dialogues from the \
                                        video have already been transcripted into the text below:\n{transcripted_text}")
    except:
        raise RuntimeError("The API key passed is invalid, please pass a valid one.")
    
    return response

def main():
    option = int(input("What do you want to do?\
        \nSet up your api key. (1)\
        \nGet the summary for a youtube video. (2)\
        \nExit. (3)\n"))
    
    if option == 1:
        key = input("Insert your google ai api key.\n")
        with open('api_key.txt', 'w') as api_file:
            api_file.write(key)

    if option == 2:
        api_key = get_api_key()

        video_id = get_video_id()

        transcripted_text = get_transcripted_text(video_id)

        video_summary = get_video_summary(transcripted_text, api_key)

        with open('response.md', 'w') as md_file:
            md_file.write(video_summary.text)

        print("The summary of the video is on the response.md file.")

    if option == 3:
        return

if __name__ == '__main__':
    main()