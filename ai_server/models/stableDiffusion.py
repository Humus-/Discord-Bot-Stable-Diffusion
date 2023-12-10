class StableDiffusion(Model):
	def __init__(self, useRefiner = True):
		Model.__init__(self)
		self.name = 'stable-diffusion-xl-base-1'
		self.description = 'Stable diffusion xLarge model'
		self.refiner = None
		self.useRefiner = useRefiner

	def setup_model(self):
		self.model_obj = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",
			torch_dtype=torch.float16,
			use_safetensors=True,
			variant="fp16")
		self.model_obj.to("cuda")

		if useRefiner:
			self.refiner = DiffusionPipeline.from_pretrained(
				"stabilityai/stable-diffusion-xl-refiner-1.0",
				text_encoder_2=self.model_obj.text_encoder_2,
				vae=self.model_obj.vae,
				torch_dtype=torch.float16,
				use_safetensors=True,
				variant="fp16",
			)

			self.refiner.to("cuda")

	def inference(self, prompt):
		n_steps = 40
		high_noise_frac = 0.8

		if not prompt:
			prompt = "A majestic lion like the statue of liberty"

		# run both experts
		image = base(
		    prompt=prompt,
		    num_inference_steps=n_steps,
		    denoising_end=high_noise_frac,
		    output_type="latent",
		).images

		if useRefiner:
			image = refiner(
			    prompt=prompt,
			    num_inference_steps=n_steps,
			    denoising_start=high_noise_frac,
			    image=image,
			).images

		image = image[0]

		return image