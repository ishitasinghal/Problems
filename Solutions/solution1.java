public class Main
{
	public static void main(String[] args) {

for (int i =1; i<8; i++)
{
    for (int j = 1; j<=i; j++)
    {
    System.out.print("*");
    }

    for (int j =1;j<16-i*2;j++)
    {
        System.out.print("#");
    }

    
    for (int l = 1;l<=i;l++)
    {
    System.out.print("*");
    }
    System.out.println();

}  
}
}
