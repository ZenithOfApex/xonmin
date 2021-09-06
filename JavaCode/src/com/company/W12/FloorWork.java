package com.company.W12;

import java.util.Scanner;

public class FloorWork {

    public void exe(){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int [] arr = new int[N+1]; // 2XN 타일 일 때 만들 수 있는 방법 수 젖아


        arr[1] = 1;
        arr[2] =3;

        for(int i =3 ; i< N+1; i++){
            arr[i] = (arr[i-1] + 2*arr[i-2] ) % 796796;
        }

        System.out.println(arr[N]);
    }
}
