using ImageAugumentation;

namespace Terminal
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var inputDirectory = "E:/!!IRL/School/!!University/UofU/ECE5960/veinfinder/Images/Training Images/Input";
            var outputDirectory = "E:/!!IRL/School/!!University/UofU/ECE5960/veinfinder/Images/Training Images/Annotations";

            var imageAugmentor = new AugmentationObject();
            imageAugmentor.AugmentImages(inputDirectory, outputDirectory);

            Console.WriteLine("Image augmentation completed.");
        }
    }
}