using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;

namespace ImageAugumentation
{
    public class AugmentationObject
    {
        public void AugmentImages(string inputDirectory, string outputDirectory)
        {
            AugmentImagesInDirectory(inputDirectory);
            AugmentImagesInDirectory(outputDirectory);
        }

        private void AugmentImagesInDirectory(string directory)
        {
            var files = Directory.GetFiles(directory, "*.jpg");

            foreach (var file in files)
            {
                var image = Image.FromFile(file);
                var rotatedImage = RotateImage(image, 180);

                var newFileNameRotation = Path.GetFileNameWithoutExtension(file) + "rotate180.jpg";
                var newFilePathRotation = Path.Combine(directory, newFileNameRotation);

                SaveImage(rotatedImage, newFilePathRotation, ImageFormat.Jpeg);

                image = Image.FromFile(file);
                var flippedImageVertical = FlipImageVertically(image);

                var newFileNameFlippedVertical = Path.GetFileNameWithoutExtension(file) + "verticalflip.jpg";
                var newFilePathFlippedVertical = Path.Combine(directory, newFileNameFlippedVertical);

                SaveImage(flippedImageVertical, newFilePathFlippedVertical, ImageFormat.Jpeg);

                image = Image.FromFile(file);
                var flippedImage = FlipImage(image);

                var newFileNameFlipped = Path.GetFileNameWithoutExtension(file) + "horizontalflip.jpg";
                var newFilePathFlipped = Path.Combine(directory, newFileNameFlipped);

                SaveImage(flippedImage, newFilePathFlipped, ImageFormat.Jpeg);
            }

            files = Directory.GetFiles(directory, "*.jpg");

            foreach (var file in files)
            {
                var image = Image.FromFile(file);
                var positions = new[] { "TopLeft", "TopRight", "Center", "BottomLeft", "BottomRight" };

                foreach (var position in positions)
                {
                    var zoomedImage = ZoomImage(image, 1.25f, position);

                    var newFileNameZoomed = Path.GetFileNameWithoutExtension(file) + $"zoomed{position}.jpg";
                    var newFilePathZoomed = Path.Combine(directory, newFileNameZoomed);

                    SaveImage(zoomedImage, newFilePathZoomed, ImageFormat.Jpeg);
                }

            }
        }

        private Image RotateImage(Image image, float angle)
        {
            var rotatedImage = new Bitmap(image.Width, image.Height);

            using (var g = Graphics.FromImage(rotatedImage))
            {
                g.TranslateTransform(image.Width / 2, image.Height / 2);
                g.RotateTransform(angle);
                g.TranslateTransform(-image.Width / 2, -image.Height / 2);
                g.DrawImage(image, new Point(0, 0));
            }

            return rotatedImage;
        }

        private Image FlipImage(Image image)
        {
            image.RotateFlip(RotateFlipType.RotateNoneFlipX);
            return image;
        }

        private Image FlipImageVertically(Image image)
        {
            image.RotateFlip(RotateFlipType.RotateNoneFlipY);
            return image;
        }

        private Image ZoomImage(Image image, float scale, string position)
        {
            var scaleWidth = (int)(image.Width * scale);
            var scaleHeight = (int)(image.Height * scale);

            var scaledImage = new Bitmap(scaleWidth, scaleHeight);

            using (var g = Graphics.FromImage(scaledImage))
            {
                g.DrawImage(image, 0, 0, scaleWidth, scaleHeight);
            }

            var cropX = position switch
            {
                "TopLeft" => 0,
                "TopRight" => scaleWidth - image.Width,
                "Center" => (scaleWidth - image.Width) / 2,
                "BottomLeft" => 0,
                "BottomRight" => scaleWidth - image.Width,
                _ => throw new ArgumentException("Invalid position"),
            };

            var cropY = position switch
            {
                "TopLeft" => 0,
                "TopRight" => 0,
                "Center" => (scaleHeight - image.Height) / 2,
                "BottomLeft" => scaleHeight - image.Height,
                "BottomRight" => scaleHeight - image.Height,
                _ => throw new ArgumentException("Invalid position"),
            };

            var rect = new Rectangle(cropX, cropY, image.Width, image.Height);

            return CropImage(scaledImage, rect);
        }

        private Image CropImage(Image img, Rectangle cropArea)
        {
            var bmpImage = new Bitmap(img);
            return bmpImage.Clone(cropArea, bmpImage.PixelFormat);
        }

        private void SaveImage(Image image, string filePath, ImageFormat format)
        {
            image.Save(filePath, format);
        }
    }
}