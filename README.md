# Enhanced End-To-End Video Editing

This repository is forked from [Tune-A-Video](https://arxiv.org/abs/2212.11565).


## Setup

### Requirements

```shell
pip install -r requirements.txt
```

Installing [xformers](https://github.com/facebookresearch/xformers) is highly recommended for more efficiency and speed on GPUs. 
To enable xformers, set `enable_xformers_memory_efficient_attention=True` (default).

### Weights

**[Stable Diffusion]** [Stable Diffusion](https://arxiv.org/abs/2112.10752) is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input. The pre-trained Stable Diffusion models can be downloaded from Hugging Face (e.g., [Stable Diffusion v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4), [v2-1](https://huggingface.co/stabilityai/stable-diffusion-2-1)). You can also use fine-tuned Stable Diffusion models trained on different styles (e.g, [Modern Disney](https://huggingface.co/nitrosocke/mo-di-diffusion), [Anything V4.0](https://huggingface.co/andite/anything-v4.0), [Redshift](https://huggingface.co/nitrosocke/redshift-diffusion), etc.).

**[DreamBooth]** [DreamBooth](https://dreambooth.github.io/) is a method to personalize text-to-image models like Stable Diffusion given just a few images (3~5 images) of a subject. Tuning a video on DreamBooth models allows personalized text-to-video generation of a specific subject. There are some public DreamBooth models available on [Hugging Face](https://huggingface.co/sd-dreambooth-library) (e.g., [mr-potato-head](https://huggingface.co/sd-dreambooth-library/mr-potato-head)). You can also train your own DreamBooth model following [this training example](https://github.com/huggingface/diffusers/tree/main/examples/dreambooth). 


## Usage

### Training

To fine-tune the text-to-image diffusion models for text-to-video generation, run this command:

```bash
accelerate launch train_vmodel.py --config="configs/tiger-forest.yaml"
```

Note: Tuning a 24-frame video usually takes `300~500` steps, about `10~15` minutes using one A100 GPU. 
Reduce `n_sample_frames` if your GPU memory is limited.

## Results

<table border="0" width="100%">
    <tr>
        <td>
            <img src="https://github.com/npp058/videogen/blob/main/results/output_frames/A%20car%20is%20moving%20on%20an%20empty%20road%20from%20left%20to%20right.jpg" alt="Image 1" width="800"/>
        </td>
        <td rowspan="2">A <i>red car</i> moving on the road from <i>left to right</i></td>
        <td rowspan="2">A <i>yellow jeep</i> moving on the road from <i>left to right</i></td>
    </tr>
    
    

</table>




## Shoutouts

- This code builds on [diffusers](https://github.com/huggingface/diffusers). Thanks for open-sourcing!
