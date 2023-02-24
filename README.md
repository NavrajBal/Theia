# Theia Ocular
## Believe Leadership Course
This project was made as a project for the believe leadership course in which it won first place.
To see the video highlihgting the project please visit: http://y2u.be/6vZBQaL0P_M

## Our Inspiration for it
What inspired the team to create this project, was the fact that many people around the world are misdiagnosed with different types of ocular diseases, which leads to patients getting improper treatments and ultimately leading to visual impairment (blindness). With the help of Theia, we can properly diagnose patients and find out whether or not they have any sort of ocular diseases. This will also help reduce the conflicts of incorrectly diagnosed patients around the world. Our eyes are an important asset to us human beings, and with the help of Theia, we can help many individuals around the world protect their eyes and have a clear vision of the world around them. Additionally, with the rise of COVID-19, leaving the house is very difficult due to the government restrictions. We wanted to reduce constant trips between optometrists and ophthalmologists with Theia due to the diagnosis being performed at the optometrists’ eye clinic, leading to fewer people in buildings and fewer gatherings.

## What it is 
Theia is a tool created for optometrists to identify ocular diseases directly through a web application. So how does it work? Theia’s backend framework is designed using Flask and the front end was created using plain HTML, CSS, and JavaScript. The computer vision solution was created using TensorFlow and was exported as a TensorFlow JS file to use on the browser. When an image is uploaded to Theia, the image is converted into 224 by 224 tensor matrix. When the predict button is clicked the TensorFlow model is called with its weights, and a javascript prediction promise is returned. Which is then fetched and returned to the user in a visual bar graph format.
