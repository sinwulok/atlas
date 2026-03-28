import torch
from .backbones.mcl_dnn import MCLDNN
from .backbones.sa_cnn import SACNN
from .backbones.iq_former import IQFormer
from .gated_fusion import GatedFusionFormer

def build_model(model_name, config):
    """
    輸入模型名稱與配置，回傳統一接口的模型物件。
    確保輸出均為 (Batch, Num_Classes)
    """
    registry = {
        'mcl_dnn': MCLDNN,
        'sa_cnn': SACNN,
        'iq_former': IQFormer,
        'gff_v3': GatedFusionFormer
    }
    
    if model_name not in registry:
        raise ValueError(f"實驗模型 [{model_name}] 不在註冊表中。")
        
    return registry[model_name](**config)