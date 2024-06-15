
from trackers import Tracker
from utils.video_utils import read_video, save_video




def main():
    # Read video
    video_frames = read_video("input_videos/08fd33_4.mp4")
    #initializing the tracker
    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')

    

    output_video_frames = tracker.draw_annotations(video_frames, tracks)


    # Save video
    save_video(output_video_frames, "output_videos/output_video.avi")

if __name__ == "__main__":
    main()
