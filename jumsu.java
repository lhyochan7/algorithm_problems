class jumsu {

    int factorial(int n) {
        int sum = 1;
        for(int i =n; i>0; i--) {
            sum*=i;
        }
        return sum;
    }

    boolean isPrime(int n) {
        for(int i = 2; i<n; i++) {
            if (n%i==0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String args[]) {
        int jumsu = 100;

        if (jumsu >= 90)
            System.out.println("A");
        else if (jumsu >= 80)
            System.out.println("B");
        else if (jumsu >= 70)
            System.out.println("C");
        else if (jumsu >= 60)
            System.out.println("D");
        else
            System.out.println("F");

        switch(jumsu/10) {
            case 10:
            case 9:
                System.out.println("A");
                break;
            case 8:
                System.out.println("B");
                break;
            case 7:
                System.out.println("C");
                break;
            case 6:
                System.out.println("D");
                break;
            default:
                System.out.println("F");
                break;
        }

        System.out.println(isPrime(12));

    }

}
