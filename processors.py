
from utils import rotate
import dlib
import cv2
import os

def save_faces(frame, output, verbose=False):
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		
	detector = dlib.get_frontal_face_detector()
	rects = detector(gray, 0)

	i=1
	while len(rects) is 0 and i<4:
		gray = rotate(gray,i)
		frame = rotate(frame,i)
		rects = detector(gray, 0)
		i+=1

	for (_, rect) in enumerate(rects):
		l_x = int(rect.tl_corner().x - rect.tl_corner().x*0.1)
		t_y = int(rect.tl_corner().y - rect.tl_corner().y*0.2)
		r_x = int(rect.br_corner().x + rect.br_corner().x*0.1)
		b_y = int(rect.br_corner().y + rect.br_corner().y*0.1)
		face_image = frame[t_y:b_y , l_x:r_x, :]

		cv2.imwrite(output, face_image)
		if verbose:
			print("[INFO] saved {}".format(output))

# TODO add a progress bar
def process_image_folder(input_folder, output, verbose=False):
	processed = 0
	len_folder = len(os.listdir(input_folder))

	for name in os.listdir(input_folder):
		path_image = os.path.join(input_folder, name)
		if not os.path.isfile(path_image):
			continue
			
		path2save = os.path.sep.join([output,
			"{}.png".format(len_folder+processed)])

		save_faces(cv2.imread(path_image), path2save, verbose=verbose)
		processed+=1

# TODO add a progress bar
def process_video(video_stream, output, skip, verbose=False):
	vs = cv2.VideoCapture(video_stream)
	read = 0
	processed = 0

	len_folder = len(os.listdir(output))
	
	# loop over frames from the video file stream
	while(vs.isOpened()):
		# grab the frame from the file
		(success, frame) = vs.read()

		if not success:
			break

		read += 1
		if read % skip != 0:
			continue

		path2save = os.path.sep.join([output,
			"{}.png".format(len_folder+processed)])
		processed+=1	
		save_faces(frame, path2save, verbose=verbose)

	vs.release()
	cv2.destroyAllWindows()

