
public class demo {

     public static void main(String[] args) {
        int n = 54321123;
        int rev = 0, rem = 0;

        while(n > 0)
        {
            rem = n % 10;
            n = n / 10;
            rev =rev * 10 + rem;
        }
        System.out.println(rev);


    }
}