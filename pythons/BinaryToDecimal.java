import java.util.Scanner;
public class BinaryToDecimal {
    public static void main(String[] args) {
        System.out.println("Enter the binary no. one by one");
        int count=0;
        double output;
        String in;

        String [] arr= new String[16];
        Scanner sc=new Scanner(System.in);
        while(count<=15){
            in=sc.next();
            if(in.equals("0") || in.equals("1")){
                arr[count]=in;
                count++;
            }
            else System.out.println("Wrong input , Please input again");
        }
        String binary=arr[15];
        for(int i=14; i>=0;i--){
            binary=arr[i]+ binary;
        }
        output=Integer.parseInt(binary,2);
        System.out.println("The decimal equivalent for "+binary+" is "+output);

    }
}