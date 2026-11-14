class coordinates:
    def __init__(self,width,height):
        self.center_x=width//2
        self.center_y=height//2
    def to_pixel(self,position):
        x,y=position
        pixel_x=self.center_x+x
        pixel_y=self.center_y-y
        return int(pixel_x),int(pixel_y)
    def to_physics(self,pixel):
        px,py=pixel
        x=px-self.center_x
        y=self.center_y-py
        return x,y

if __name__=="__main__":
    cor=coordinates(100,200)
    print(cor.to_physics,cor.to_pixel)
        