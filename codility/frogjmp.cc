int solution(int X, int Y, int D) {
    int dist = Y - X;
    if(dist % D == 0)
        return dist / D;
    return dist / D + 1;    
}
