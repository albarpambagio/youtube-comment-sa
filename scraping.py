from youtube_comment_downloader import YoutubeCommentDownloader
import json

def download_youtube_comments(video_id, output_file, max_comments=3500):
    """
    Downloads YouTube comments and saves to JSON file
    
    Args:
        video_id (str): YouTube video ID (e.g., "SzXMacu80o8")
        output_file (str): Path to output JSON file
        max_comments (int): Maximum number of comments to download
    """
    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_video_id(
        video_id=video_id,
        sort_by=0,  # 0 = newest first, 1 = top comments
        limit=max_comments
    )
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(list(comments), f, ensure_ascii=False, indent=2)
    
    print(f"Successfully saved {max_comments} comments to {output_file}")

# Usage equivalent to your CLI command
download_youtube_comments(
    video_id="SzXMacu80o8",
    output_file="SzXMacu80o8.json",
    max_comments=3500
)