from processors import process_image_folder
from processors import process_video
from utils import get_inputs
from pathlib import Path
import sys

args = get_inputs()

if not args["input_video"] and not args["input_folder"]:
	print('--input_video or --input_folder is required')
	sys.exit()

path = Path(args["output"])
path.mkdir(parents=True, exist_ok=True)

if args["input_video"]:
	process_video(args["input_video"], args["output"], args["skip"], verbose=args["verbose"])
if args["input_folder"]:
	process_image_folder(args["input_folder"], args["output"], verbose=args["verbose"])
