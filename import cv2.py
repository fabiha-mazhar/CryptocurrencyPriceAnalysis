import cv2
import matplotlib.pyplot as plt

# Correct local path (if file is in the same folder)
input_image1 = cv2.imread('misterbean.jpg', 1)   # Color
input_image2 = cv2.imread('misterbean.jpg', 0)   # Grayscale

# Check if image loaded
if input_image1 is None or input_image2 is None:
    raise FileNotFoundError("Image not found. Check your path!")

# Display with Matplotlib
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(input_image1, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title("Colored Image")

plt.subplot(1,2,2)
plt.imshow(input_image2, cmap='gray')
plt.axis("off")
plt.title("Grayscale Image")

plt.show()

# Save results
cv2.imwrite("result1.bmp", input_image1)
cv2.imwrite("result2.bmp", input_image2)

print("Completed Successfully ...")
