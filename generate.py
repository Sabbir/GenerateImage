from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler


def generate(prompt, height=512, width=512, output="result.png", cuda=False):
    pipeline = StableDiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1",
    )
    pipeline.scheduler = DPMSolverMultistepScheduler.from_config(pipeline.scheduler.config)
    pipeline.enable_attention_slicing()

    number_of_steps = 7
    if cuda:
        pipeline.to("cuda")
        # We could make more steps when use GPU, in theory results will be better
        number_of_steps = 30
    else:
        pipeline.to("cpu")

    results = pipeline([prompt], height=height, width=width,
                       num_inference_steps=number_of_steps,
                       num_images_per_prompt=1)
    #results.images[0].save(output)
    return results