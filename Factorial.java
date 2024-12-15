class Factorial{
    public int fact(n){
        if(n==0 || n==1){
            return 1;
        }
        return n*fact(n-1);
    }
    public static void main(String[] args) {
        Factorial f = new Factorial();
        int result = f.fact(5);
        System.out.println(result);
    }
}