## All together

### Precompute

Lightmap

sphericalharmonics

### Soft Shadow

E:\UE\UnrealEngine_425\UnrealEngine\Engine\Source\Runtime\Renderer\Private\CapsuleShadowRendering.cpp

RenderIndirectCapsuleShadows

E:\UE\UnrealEngine_425\UnrealEngine\Engine\Source\Runtime\Renderer\Private\DistanceFieldAmbientOcclusion.cpp

RenderDFAOAsIndirectShadowing

### GI

e:\UE\UnrealEngine_425\UnrealEngine\Engine\Source\Runtime\Renderer\Private\IndirectLightRendering.cpp

const bool bApplyRTGI = ShouldRenderRayTracingGlobalIllumination(View);

const bool bApplySSGI = ShouldRenderScreenSpaceDiffuseIndirect(View);

const bool bApplySSAO = SceneContext.bScreenSpaceAOIsValid;

const bool bApplyRTAO = ShouldRenderRayTracingAmbientOcclusion(View) && Views.Num() == 1;

#### TranslucencyVolume (不是GI)

InjectAmbientCubemapTranslucentVolumeLighting

FilterTranslucentVolumeLighting

#### LPV

E:\UE\UnrealEngine_425\UnrealEngine\Engine\Source\Runtime\Renderer\Private\CompositionLighting\CompositionLighting.cpp

ProcessLpvIndirect

#### SSR

E:\UE\UnrealEngine_425\UnrealEngine\Engine\Source\Runtime\Renderer\Private\IndirectLightRendering.cpp

RenderRayTracingReflections

RenderScreenSpaceReflections

DenoiseReflections or TAA

### AtomosphericFog

E:\UE\UnrealEngine_425\UnrealEngine\Engine\Source\Runtime\Renderer\Private\AtmosphereRendering.cpp

RenderAtmosphere

E:\UE\UnrealEngine_425\UnrealEngine\Engine\Source\Runtime\Renderer\Private\SkyAtmosphereRendering.cpp

RenderSkyAtmosphere

E:\UE\UnrealEngine_425\UnrealEngine\Engine\Source\Runtime\Renderer\Private\FogRendering.cpp

RenderFog height fog

### PostProcess

https://docs.unrealengine.com/4.27/en-US/RenderingAndGraphics/PostProcessEffects/

TAA

Tone Map

### Shading Model

## 总结