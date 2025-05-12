function solution(sizes) {
    return Math.max(...sizes.map(([w, h]) => Math.max(w, h)))*Math.max(...sizes.map(([w, h]) => Math.min(w, h)));
}