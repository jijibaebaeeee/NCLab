
import hydra
from omegaconf import DictConfig, OmegaConf  # 또 다른 구성 프레임워크

# 현재 프로젝트의 구성 파일이 어디에 있는지 알려주는 것 conf 라는 디렉토리
# python main을 실행하면 사용할 구성이 무엇인지 설정 -> base 파일
# 코드에서 경고가 발생하는 것을 방지하기 위해 버전 기준을 None 으로 함
# 이 데코레이터가 수행할 작업은 구성을 구문 분석하거나 부분적으로 구문 분석하고 이를 메인으로 전달하는 것
hydra.main(config_path="conf", config_name="base", version_base=None)
def main(cfg: DictConfig):

    print(OmegaConf.to_yaml(cfg))    # yaml을 수행할 수 있도록 구성을 인쇄하는 것  // 이해 못한 부분 2번째 동영상 14:11

# if __name__ == "__main__":

#     main()
    