from flask import Flask, request, render_template
import numpy as np
from skimage.feature import greycomatrix, greycoprops
application = Flask(__name__)
image = np.random.randint(0, 5, size=(4, 4))

print(image)
range = [1]
ved = [0]
result = greycomatrix(image, [1], [0, np.pi/4], levels=image.max()+1)
glcmMatrix = result[:, :, 0, 0]
print(glcmMatrix)
print(result[:, :, 0, 1])


@application.route('/')
def hello_world():  # put application's code here
    return render_template('GLCMfile.html', Matrix1=image, GlcmMatrix=glcmMatrix, Distance=1, Angle=0)


@application.route('/', methods=['POST'])
def my_form_post():
    distance = int(request.form['distance'])
    print(distance)
    angle = request.form['angle']
    bh = 0
    print(angle)
    if angle == "45":
        bh = 3 * np.pi / 4
    elif angle == "90":
        bh = np.pi / 2
    elif angle == "135":
        bh = np.pi / 4
    print(bh)
    out = greycomatrix(image, [distance], [bh], levels=image.max() + 1)
    finalmatrix = np.transpose(out[:, :, 0, 0])
    return render_template('GLCMfile.html', Matrix1=image, GlcmMatrix=finalmatrix, Distance=distance, Angle=angle)


@application.route('/glcm')
def glcm_ui():
    return render_template('GLCMfile.html', Matrix1=image, GlcmMatrix=glcmMatrix)


if __name__ == '__main__':
    application.run()
