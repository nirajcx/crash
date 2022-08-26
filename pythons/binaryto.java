public class binaryto {
    public static void main(String[] args) throws Exception{
        System.out.println("Enter the 16_bit binary no.");
        int count=0;
        double output;
        char in;

        char [] arr= new char[16];
        //Scanner sc=new Scanner(System.in);
        while(count<=15){
            in= (char) System.in.read();
            if(in=='0' || in=='1'){
                arr[count]=in;
                count++;
            }
            else System.out.println("Wrong input , Please input again");
        }
        String binary="";
        for(int i=15; i>=0;i--){
            binary=arr[i]+ binary;
        }
        output=Integer.parseInt(binary,2);
        System.out.println("The decimal equivalent for "+binary+" is "+output);
    }
}