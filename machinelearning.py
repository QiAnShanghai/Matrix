from PIL import Image
import Mat

class Neural:
	def __init__(self,layersizes):
		self.layersizes = []
		self.layers = []
		for i in layersizes:
			self.layersizes.append(i)
		for i in range(len(self.layers-1))
			a = self.layers(i+1)
			b = self.layers(i)
			A = []
			for j in range(a):
				aa = []
				for k in range(b):
					aa.append(0)
				A.append(aa)
			self.layers.appennd(Mat.Mat(A))
			
