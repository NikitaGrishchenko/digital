export default class waveNoise {
  private waveSet: number[];
  private waveSpeed: number;

  constructor(waveSpeed = 0.3) {
    this.waveSet = [];
    this.waveSpeed = waveSpeed;
  }

  addWaves(requiredWaves: number) {
    for (let i = 0; i < requiredWaves; i++)
      this.waveSet.push(Math.random() * 360);
  }
  getWave() {
    let blendedWave = 0;
    this.waveSet.forEach((e) => {
      blendedWave += Math.sin((e / 180) * Math.PI);
    });
    return (blendedWave / this.waveSet.length + 1) / 2;
  }
  update() {
    this.waveSet.forEach((e, i) => {
      const r = Math.random() * (i + 1) * this.waveSpeed;
      this.waveSet[i] = (e + r) % 360;
    });
  }
}
