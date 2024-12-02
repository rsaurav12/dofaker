WEIGHT_URLS = {
    'buffalo_l':
    'https://github.com/rsaurav12/dofaker/releases/download/release/buffalo_l.zip',
    'buffalo_s':
    'https://github.com/rsaurav12/dofaker/releases/download/release/buffalo_s.zip',
    'buffalo_sc':
    'https://github.com/rsaurav12/dofaker/releases/download/release/buffalo_sc.zip',
    'inswapper':
    'https://github.com/rsaurav12/dofaker/releases/download/release/inswapper_128.onnx',
    'gfpgan':
    'https://github.com/rsaurav12/dofaker/releases/download/release/GFPGANv1.3.onnx',
    'bsrgan':
    'https://github.com/rsaurav12/dofaker/releases/download/release/bsrgan_4.onnx',
    'openpose_body':
    'https://github.com/rsaurav12/dofaker/releases/download/release/openpose_body.onnx',
    'pose_transfer':
    'https://github.com/rsaurav12/dofaker/releases/download/release/pose_transfer.onnx',
}


def get_model_url(model_name):
    return WEIGHT_URLS[model_name]
