# AI Journey Lab

Andrej Karpathy의 [Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero/tree/master) 학습용입니다.
ai, deep learning 의 기본 개념을 직접 구현. 학습 과정과 실험 결과를 주피터 노트북에 기록합니다.

## 프로젝트

- **[micrograd](micrograd/engine.ipynb)**: 스칼라 값의 연산 그래프와 역전파를 구현하고, 이를 이용해 Neuron, Multi-Layer Perceptron(MLP)을 구성합니다.
- **[makemore](makemore/part1_bigrams.ipynb)**: 이름 데이터의 문자 쌍(bigram) 빈도로 확률 모델을 만들고, 새 이름을 생성하며 모델의 손실을 계산까지 진행.

`makemore`에서 사용하는 이름 데이터는 저장소에 포함되어 있지 않습니다.
