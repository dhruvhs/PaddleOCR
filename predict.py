import tools.infer.utility as utility
from tools.infer.predict_system import main

def predict():
    args = utility.parse_args()
    args.use_gpu = False
    args.use_onnx = True
    args.det_model_dir = "./inference/det_onnx/model.onnx"
    args.rec_model_dir = "./inference/rec_onnx/model.onnx"
    # args.image_dir = "/Users/dhruv/Downloads/d.png"
    args.image_dir = "/Users/dhruv/Downloads/test-designs-vertical"
    args.draw_img_save_dir = "test-designs-vertical"
    main(args)


def text_detector(img):
    pass


if __name__ == '__main__':
    predict()