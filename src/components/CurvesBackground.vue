<template>
  <div class="curves-wrapper" :style="`z-index: ${zIndex}`">
    <canvas id="curves" ref="cnv"></canvas>
  </div>
</template>

<script lang="ts">
  import waveNoise from 'hooks/useAnimation';
  import { defineComponent, onMounted, onUnmounted, ref } from 'vue';

  type size = { width: number; height: number; cx: number; cy: number };
  type curveParam = {
    startX: number;
    startY: number;
    controlX1: number;
    controlY1: number;
    controlX2: number;
    controlY2: number;
    endX: number;
    endY: number;
    alpha: number;
    hue: number;
  };

  export default defineComponent({
    name: 'CurvesBackground',
    props: {
      waveSpeed: {
        type: Number,
        default: 0.07
      },
      wavesToBlend: {
        type: Number,
        default: 4
      },
      curvesNum: {
        type: Number,
        default: 50
      },
      framesToMove: {
        type: Number,
        default: 120
      },
      zIndex: {
        type: String,
        default: '-1'
      }
    },
    setup(props) {
      let cnv = ref<HTMLCanvasElement>();
      let ctx: CanvasRenderingContext2D;
      let size: size;
      let controls: waveNoise[] = [];
      const controlsNum = 5;

      const setCanvasSize = (): void => {
        size = {
          width: window.innerWidth,
          height: window.innerHeight,
          cx: window.innerWidth / 2,
          cy: window.innerHeight / 2
        };
        if (cnv.value) {
          cnv.value.width = size.width;
          cnv.value.height = size.height;
        }
      };
      const createCanvas = (): void => {
        ctx = cnv.value?.getContext('2d') ?? new CanvasRenderingContext2D();
        setCanvasSize();
        window.addEventListener('resize', () => {
          setCanvasSize();
        });
      };
      const createControls = (): void => {
        let control: waveNoise;
        for (let i = 0; i < controlsNum + props.curvesNum; i++) {
          control = new waveNoise(props.waveSpeed);
          control.addWaves(props.wavesToBlend);
          controls.push(control);
        }
      };
      const drawCurve = (curveParam: curveParam): void => {
        ctx.strokeStyle = `rgba(${curveParam.hue}, 43, 252, ${curveParam.alpha})`;
        ctx.beginPath();
        ctx.moveTo(curveParam.startX, curveParam.startY);
        ctx.bezierCurveTo(
          curveParam.controlX1,
          curveParam.controlY1,
          curveParam.controlX2,
          curveParam.controlY2,
          curveParam.endX,
          curveParam.endY
        );
        ctx.stroke();
      };
      const updateCurves = (): void => {
        let c = controls;
        let curveParam: curveParam;
        for (let i = 0; i < props.curvesNum; ++i) {
          curveParam = {
            startX: size.width < 768 ? -size.width / 2 : 0,
            startY:
              size.width < 768
                ? (size.height / 1.5 / props.curvesNum) * i
                : ((size.cy * 2) / props.curvesNum) * i,
            controlX1: c[0].getWave() * size.width,
            controlY1: c[1].getWave() * size.height,
            controlX2: c[2].getWave() * size.width,
            controlY2: c[3 + i].getWave() * size.height,
            endX: size.width < 768 ? size.width * 2 : size.width,
            endY: (size.height / 1.5 / props.curvesNum) * i,
            alpha: c[3 + i].getWave(),
            hue: (360 / props.curvesNum) * i
          };
          drawCurve(curveParam);
        }
      };
      const updateCanvas = (): void => {
        ctx.fillStyle = '#ffffff00';
        ctx.clearRect(0, 0, size.width, size.height);
        ctx.fillRect(0, 0, size.width, size.height);
      };
      const updateControls = (): void => {
        controls.forEach((e: waveNoise) => e.update());
      };
      const updateAnimation = (): void => {
        updateCanvas();
        updateCurves();
        updateControls();
        window.requestAnimationFrame(() => updateAnimation());
      };

      onMounted(() => {
        createCanvas();
        createControls();
        updateAnimation();
      });

      onUnmounted(() => {
        window.removeEventListener('resize', setCanvasSize);
        window.cancelAnimationFrame;
      });

      return {
        cnv,
        setCanvasSize
      };
    }
  });
</script>
