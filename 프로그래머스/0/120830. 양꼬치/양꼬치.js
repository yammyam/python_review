function solution(n, k) {
  if (n < 10) {
    let nSum = n * 12000;
    let kSum = k * 2000;
    return nSum + kSum;
  }
  else if (n >= 10) {
    let nSum = n * 12000;
    let kSum = k * 2000;
    return nSum + kSum-((Math.floor(n/10))*2000);
  }
}