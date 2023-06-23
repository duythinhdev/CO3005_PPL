// run everything in here
package java_gen_code;


public class X extends java_gen_code.y {

    X(int c) {
        super(c);
        //TODO Auto-generated constructor stub
    }

    static int d = 0;
    int xd;
    int swap(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
        this.xd = a;
        for (int i = 0; i < 10; i++) {
            int c = 5;
            a+= 1;
            c +=2;
            this.xd = c;
            if (a > b) {
                return a;
            }
            if (b > a) {
                break;
            }
            X.d = a;
        }
        return a;
    }
    
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        System.out.println("Hello World");
    }

}

