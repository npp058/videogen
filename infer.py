from vmodel.pipelines.pipeline_eve import EvePipeline
from vmodel.models.unet import UNet3DConditionModel
from vmodel.util import save_videos_grid
import torch

pretrained_model_path = "./checkpoints/stable-diffusion-v1-4"
my_model_path = "./outputs/tiger-forest"
unet = UNet3DConditionModel.from_pretrained(my_model_path, subfolder='unet', torch_dtype=torch.float16).to('cuda')
pipe = EvePipeline.from_pretrained(pretrained_model_path, unet=unet, torch_dtype=torch.float16).to("cuda")
pipe.enable_xformers_memory_efficient_attention()
pipe.enable_vae_slicing()

prompt = "a panda is surfing"

ddim_inv_latent = torch.load(f"{my_model_path}/inv_latents/ddim_latent-25.pt").to(torch.float16)
video = pipe(prompt, latents=ddim_inv_latent, video_length=24, height=512, width=512, num_inference_steps=10, guidance_scale=12.5).videos

save_videos_grid(video, f"./{my_model_path}/video/{prompt}.gif")