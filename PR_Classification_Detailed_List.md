# TensorRT-LLM PR分类详细列表

**生成时间**: 2026-01-22
**数据来源**: 基于1,485个PR的分析，其中451个有完整CI+Review数据

---

## 统计摘要

- **直接合入的PR**: 364 个 (80.7%)
- **被阻塞的PR**: 87 个 (19.3%)
- **总计**: 451 个

**定义说明**:
- **直接合入**: 所有CI检查通过，PR Checklist完成，标题格式正确，Review直接Approved，无任何返工
- **被阻塞**: 至少有一个卡点（CI失败/Checklist未完成/标题格式错误/Review要求修改/Pre-commit失败）

---

## 一、直接合入的PR列表 (364个)

这些PR没有经历任何打回或阻塞，顺利合入。

| PR编号 | 标题 | 提交者 | 代码变更 | 合并耗时 | 标签 |
|-------|------|--------|---------|---------|------|
| #2823 | Add R1 perf data to latest news page | laikhtewari | +7/-3 (2 files) | 0.2h | - |
| #2830 | Use NVIDIA-gha runners to collect test results for CI | tburt-nv | +33/-16 (1 files) | 27.3h | - |
| #3384 | fix: Use hmac authentication for pickle encryption | yibinl-nvidia | +118/-31 (4 files) | 186.2h | - |
| #3435 | fix: Fix the issues related to fused moe path. | hyukn | +6/-6 (2 files) | 33.0h | - |
| #3497 | fix: add kv memory size per token of draft model to calculat... | HuiGao-NV | +8/-3 (1 files) | 27.4h | - |
| #3506 | refactor: Introduce DecoderOutputBuffers per batch | Funatiq | +273/-253 (5 files) | 204.7h | - |
| #3510 | test: [CI] remove closed bugs | xinhe-nv | +0/-3 (1 files) | 5.2h | - |
| #3550 | fix: remove extraneous local docker user command | tburt-nv | +0/-4 (1 files) | 5.9h | - |
| #3553 | Clean up linear.py, mlp.py, gated_mlp.py | hlu1 | +125/-82 (7 files) | 41.5h | - |
| #3563 | fix: amend trtllm-bench command in the test | Superjomn | +1/-1 (1 files) | 22.4h | - |
| #3584 | feat: Disaggregated router class | pcastonguay | +626/-42 (9 files) | 72.4h | - |
| #3585 | fix: nvbugs/5075538: fix cross attention mask when decoder i... | VALLIS-NERIA | +1/-2 (2 files) | 7.6h | - |
| #3600 | fix: fix cublas_scaled_mm | dc3671 | +13/-7 (2 files) | 122.2h | - |
| #3642 | fix: Pick waives from main | syuoni | +3/-0 (3 files) | 0.9h | - |
| #3687 | chore: Waive disaggregated load balance | Tabrizian | +1/-0 (1 files) | 0.8h | - |
| #3691 | Report number of context tokens in one iteration | HuiGao-NV | +4/-2 (1 files) | 54.3h | - |
| #3760 | chore: add pull request template | byshiue | +74/-2 (2 files) | 19.0h | - |
| #3761 | Fix: nvbugs/5234210 ModelOpt Mixtral AWQ OOM (cherry-picking... | Barry-Delaney | +50/-4 (2 files) | 35.3h | - |
| #3765 | Add log_level for disaggregated_mpi_worker | qiaoxj07 | +6/-1 (1 files) | 7.6h | - |
| #3787 | fix: remove the unnecessary metadata changes in mtp | lfr-0531 | +2/-25 (1 files) | 4.5h | - |
| #3832 | Fix: Revert commit 25f9669 | Shixiaowei02 | +0/-13 (1 files) | 0.3h | - |
| #3841 | chore: Mass integration of release/0.19 into main | DomBrown | +457/-192 (46 files) | 116.7h | - |
| #3855 | feat: Add multimodal embedding field in LlmRequest | katec846 | +290/-164 (26 files) | 141.6h | - |
| #3859 | infra: [TRTLLM-4475][TRTLLM-4565] Add pipeline hierarchy and... | ZhanruiSunCh | +49/-14 (3 files) | 265.1h | - |
| #3863 | fix: Fix FMHA-based MLA in the generation phase and add MLA ... | jinyangyuan-nvidia | +0/-0 (0 files) | 88.9h | - |
| #3885 | feat: support multi lora adapters and TP | shaharmor98 | +274/-175 (18 files) | 275.0h | - |
| #3899 | feat: fix erros on scaffolding README | WeiHaocheng | +2/-2 (1 files) | 23.2h | - |
| #3925 | unwaive disagg tests | chuangz0 | +0/-5 (1 files) | 31.2h | - |
| #3926 | Cherry pick https://github.com/NVIDIA/TensorRT-LLM/pull/3906... | litaotju | +1/-1 (1 files) | 0.1h | - |
| #3929 | [NVBUG 5247699]Fix mixtral fp4 llmapi bug. | Tracin | +0/-1 (1 files) | 25.9h | - |
| #3972 | fix[nvbug-5228840]: Remove test cases of feature not support... | HuiGao-NV | +0/-4 (2 files) | 528.8h | - |
| #4016 | [Deepseek] Refactor Deepseek Decoder layer | hlu1 | +160/-110 (5 files) | 139.3h | - |
| #4065 | [feat/] enable attention DP in Llama4 maverick model - part ... | zihaok | +62/-22 (4 files) | 52.0h | - |
| #4074 | [fix] Loosen the thresholds of test_attention_mla | jinyangyuan-nvidia | +2/-2 (1 files) | 2.5h | - |
| #4095 | [https://nvbugspro.nvidia.com/bug/5260676]test: skip fp8 qua... | crazydemo | +1/-0 (1 files) | 63.0h | - |
| #4098 | doc: Update version switcher | kaiyux | +4/-0 (1 files) | 1.1h | - |
| #4109 | [Infra] - Update code ownership rules | chzblych | +12/-0 (1 files) | 3.6h | - |
| #4122 | [Infra] - Update code ownership rules for public APIs | chzblych | +7/-6 (1 files) | 14.9h | - |
| #4129 | docs:add torch flow supported model list. | nv-guomingz | +28/-1 (1 files) | 9.5h | - |
| #4140 | feat: Prefetch safetensors files before loading them | nvpohanh | +37/-4 (1 files) | 122.2h | - |
| #4142 | enh: Enable option in trtllm-bench build subcommand to avoid... | venkywonka | +9/-1 (1 files) | 183.9h | - |
| #4155 | Feat: support exporting softmax statistics and update the ke... | PerkzZheng | +0/-0 (0 files) | 90.7h | - |
| #4158 | Add test case for kv memory estimation | HuiGao-NV | +323/-116 (4 files) | 140.5h | - |
| #4161 | [TRTLLM-5054][fix] Removing repeated loading of input proces... | rakib-hasan | +52/-34 (2 files) | 175.0h | - |
| #4176 | test: amend default pytorch extra-llm-api-config.yml in perf... | ruodil | +6/-3 (3 files) | 1.8h | - |
| #4183 | feat: Support Mistral Small 3.1 24B VLM in TRT workflow | brb-nv | +255/-7 (8 files) | 107.6h | - |
| #4186 | test: amend regex match for perf throughput | ruodil | +4/-4 (2 files) | 0.2h | - |
| #4191 | infra: [TRTLLM-325] Prepare for NGC release - multiplatform ... | MartinMarciniszyn | +152/-81 (12 files) | 67.0h | - |
| #4206 | [CI] waive two multi-gpu test cases | QiJune | +2/-0 (2 files) | 12.4h | - |
| #4263 | Test: Improve model re-use in C++ DGX tests for CI stability | DomBrown | +353/-195 (4 files) | 146.1h | Infra |
| #4297 | chore: reduce code duplication | ixlmar | +3/-10 (1 files) | 23.4h | - |
| #4300 | [https://nvbugs/5277113][fix]genai-perf API change stress te... | dominicshanshan | +4/-11 (4 files) | 18.9h | - |
| #4348 | Fix bias shape in weightOnlyGroupwiseQuantMatmulPlugin for T... | StudyingShao | +4/-4 (1 files) | 20.0h | Community want to contribute, Community Engagement |
| #4358 | feat: Add pp support for hybrid attn/mamba model | yuxianq | +112/-54 (6 files) | 89.8h | - |
| #4370 | [AutoDeploy] eager pattern matcher new pattern | lucaslie | +162/-64 (2 files) | 18.0h | AutoDeploy |
| #4373 | [AutoDeploy] fix: proper process group clean up | lucaslie | +24/-0 (2 files) | 17.9h | AutoDeploy |
| #4376 | Remove vila test | Tabrizian | +0/-247 (5 files) | 73.0h | - |
| #4386 | doc： DS r1 min latency blog | Kefeng-Duan | +267/-0 (7 files) | 6.8h | - |
| #4393 | Fix test_fused_moe_w4afp8 | StudyingShao | +6/-20 (1 files) | 0.3h | - |
| #4394 | Feat: add chunked-attention kernels on Blackwell | PerkzZheng | +0/-0 (0 files) | 111.7h | - |
| #4400 | doc: [TRTLLM-325]Integrate the NGC image in Makefile automat... | MartinMarciniszyn | +53/-26 (9 files) | 87.7h | - |
| #4417 | test: [CI] remove closed bugs | xinhe-nv | +1/-2 (1 files) | 61.0h | - |
| #4434 | [Docs] - Reapply #4220 | chzblych | +1/-18 (2 files) | 7.4h | - |
| #4479 | tests: update api change from decoder to sampler in test | crazydemo | +4/-3 (2 files) | 22.6h | - |
| #4489 | fix: replace the image links in the blog | Shixiaowei02 | +5/-5 (1 files) | 2.2h | - |
| #4507 | fix: Fix trtllm sampler beam width bug | dcampora | +7/-6 (1 files) | 4.2h | - |
| #4508 | Chore: waive torch compile test cases of deepseek v3 lite | QiJune | +8/-0 (1 files) | 0.4h | - |
| #4535 | [TRTLLM-5070][feat] Support FP8 KV Cache Reuse for MLA | zhhuang-nv | +613/-342 (9 files) | 48.2h | - |
| #4594 | [TRTLLM-4647][fix] Fix the no fusion allreduce hanging | timlee0212 | +56/-45 (6 files) | 315.1h | - |
| #4611 | feat: Integration of Fused QKNorm+RoPE. | bobboli | +72/-32 (5 files) | 114.4h | - |
| #4613 | fix: test trtllm-bench mgmn | Superjomn | +5/-4 (4 files) | 141.2h | - |
| #4623 | [TRTLLM-1658][feat] Enable multiple response in trtllm-serve... | LinPoly | +23/-41 (4 files) | 108.9h | - |
| #4651 | feat: chunked prefill for MLA (Blackwell) | jmydurant | +2320/-40 (19 files) | 740.8h | - |
| #4663 | Add files into scan ignoreList | yiqingy0 | +7/-1 (1 files) | 1.5h | - |
| #4671 | Update the description for NGC docker images | MartinMarciniszyn | +100/-3 (2 files) | 10.3h | - |
| #4694 | use cu for fmha_v2 | qsang-nv | +4599/-5640 (8 files) | 456.8h | - |
| #4713 | fix: Mistral Small vision encoder with BS>1 | brb-nv | +91/-34 (4 files) | 6.0h | - |
| #4734 | fix: iteration logging and typing in PyExecutor | ixlmar | +25/-30 (2 files) | 43.0h | - |
| #4766 | fix: re-enable tp/pp for quickstart_advanced.py. | yuxianq | +7/-2 (2 files) | 47.2h | - |
| #4790 | [Architecture] Refactor FusedMoE | hlu1 | +3203/-2575 (24 files) | 97.0h | - |
| #4803 | Expose new tech blog about DSR1 throughput optimization to t... | juney-nvidia | +8/-5 (2 files) | 1.6h | - |
| #4818 | feat: large-scale EP(part 6: Online EP load balancer integra... | dongxuy04 | +2121/-361 (28 files) | 161.2h | - |
| #4819 | [TRTLLM-4987][feat] Support generation logits in TRTLLMSampl... | amitz-nv | +150/-75 (6 files) | 185.4h | - |
| #4832 | fix: [https://nvbugspro.nvidia.com/bug/5273945] Unwaive test... | lfr-0531 | +0/-1 (1 files) | 5.8h | - |
| #4864 | fix: Register MoeLoadBalancerConfig to serialization.py | syuoni | +1/-0 (1 files) | 0.4h | - |
| #4876 | feat: Add support for fp8 rowwise quantization | achartier | +497/-126 (13 files) | 260.0h | Community want to contribute, Community Engagement |
| #4896 | chore: bump version to 0.21.0rc1 | ZhanruiSunCh | +3/-3 (3 files) | 0.8h | - |
| #4897 | fix: Fix broken vanilla moe since FusedMoE refactor. | yuxianq | +30/-34 (6 files) | 13.8h | - |
| #4906 | feat: Add support for YARN in NemotronNAS models | amirkl94 | +14/-6 (3 files) | 598.1h | - |
| #4920 | Only pass `fast_build=true` to non-pytorch backend | netanel-haber | +4/-1 (1 files) | 10.4h | - |
| #4921 | fix: [nvbug 5321627] handle cases when TRT backend return mo... | hchings | +5/-0 (1 files) | 26.9h | - |
| #4951 | ci: [nvbugs/5280806] Unwaive unittests/_torch. | yuxianq | +73/-53 (12 files) | 97.0h | - |
| #4969 | Resubmit #4894 | QiJune | +40/-1 (5 files) | 44.3h | - |
| #4973 | fix:https://nvbugs/5324248 | nv-guomingz | +10/-4 (2 files) | 17.9h | - |
| #4989 | tests: fix some typo and limitation on test cases | crazydemo | +2/-1 (2 files) | 89.1h | - |
| #5009 | [Infra] - Update JNLP container config | chzblych | +22/-7 (5 files) | 0.4h | - |
| #5020 | fix #4974: A thread leak issue in scaffolding unittest | ccs96307 | +2/-0 (1 files) | 845.2h | Community want to contribute |
| #5042 | [fix] Unwaive test_llama_eagle3 | mikeiovine | +0/-1 (1 files) | 31.1h | - |
| #5054 | [AutoDeploy] Merge Feature Branch Week 3 | lucaslie | +417/-422 (11 files) | 17.5h | AutoDeploy |
| #5071 | CI: waive test_ad_build_small_multi | QiJune | +2/-0 (1 files) | 0.2h | - |
| #5122 | feat: Support post_proc for bench | kaiyux | +26/-14 (6 files) | 93.2h | - |
| #5125 | [test] add nvfp4 DeepSeek-V3-Lite-mtp tests | lfr-0531 | +108/-44 (10 files) | 184.6h | - |
| #5128 | [TRTLLM-5835][feat] Optimized Mamba2Mixer prefill | tomeras91 | +183/-156 (4 files) | 120.9h | - |
| #5142 | Add Wechat_Group_QR_Code.png to docs/source/media and main p... | AdamzNV | +1/-0 (2 files) | 184.5h | - |
| #5159 | [TRTLLM-5758] test: Add Bielik-11B-v2.2 Model Support | Wanli-Jiang | +81/-0 (5 files) | 141.4h | - |
| #5183 | feat: MoE trtllm backend kernel update | rosenrodt | +3650/-1459 (88 files) | 74.5h | - |
| #5188 | optimize memset before alltoall communication | dongxuy04 | +44/-12 (1 files) | 20.4h | - |
| #5200 | fix: fix license bug | yunruis | +379/-27 (22 files) | 0.3h | - |
| #5209 | [fix] Fix Llama4 min-latency import error | nv-yilinf | +20/-8 (1 files) | 56.2h | - |
| #5221 | test: [CI] Add failed cases into waives.txt | xinhe-nv | +2/-0 (1 files) | 13.6h | - |
| #5230 | chore: enable moe_backend on Qwen3 test | byshiue | +50/-12 (6 files) | 70.9h | - |
| #5237 | test: add more pytorch cases in perf test | ruodil | +43/-5 (3 files) | 18.9h | - |
| #5245 | None - Some clean-ups for the automation pipeline | chzblych | +38/-53 (5 files) | 23.0h | - |
| #5258 | [enhance] Add the ability to write a request timeline. | FrankD412 | +27/-1 (3 files) | 576.6h | - |
| #5295 | chore: Refine printed info of CHECK_TYPE. | bobboli | +2/-1 (1 files) | 11.7h | - |
| #5298 | Revert "[infra] Report CI authorization errors to PR" | tburt-nv | +0/-20 (1 files) | 0.0h | Community want to contribute |
| #5307 | test: cherry-pick deepseek rcca cases in main branch | ruodil | +12/-0 (2 files) | 3.2h | - |
| #5309 | chore: bump version to 0.21.0rc3 | ZhanruiSunCh | +3/-3 (3 files) | 3.4h | - |
| #5334 | doc: Include NGC release containers in quick-start-guide.md | MartinMarciniszyn | +12/-2 (1 files) | 18.0h | - |
| #5337 | Fix CI build time increase | yunruis | +17/-11 (3 files) | 14.3h | - |
| #5360 | [Infra]Fix l0_sanity_check.yml which also as gb202 and gb203 | EmmaQiaoCh | +2/-0 (1 files) | 0.3h | - |
| #5363 | [Infra]cherry pick sanity check yml change for 5080 and 5090... | EmmaQiaoCh | +2/-0 (1 files) | 0.2h | - |
| #5378 | Fix: missing clientId when serialize and deserialize respons... | kaiyux | +18/-4 (2 files) | 94.3h | - |
| #5404 | [#5403][perf] Conditionally enable SWAP AB for speculative d... | zoheth | +119/-19 (4 files) | 191.9h | Community want to contribute |
| #5422 | Fix none response in PD | Shunkangz | +2/-1 (1 files) | 239.7h | - |
| #5428 | feat: Make benchmark_serving part of the library | kaiyux | +12/-10 (3 files) | 30.4h | - |
| #5460 | chore: bump version to 1.0.0rc1 | yiqingy0 | +3/-3 (3 files) | 3.5h | - |
| #5491 | Update trtllm-bench to support new Pytorch default. | FrankD412 | +25/-15 (6 files) | 31.4h | - |
| #5529 | feat(models): Mistral3.1 VLM pytorch backend support | 2ez4bz | +1224/-4 (8 files) | 309.3h | - |
| #5536 | [Infra] - Waive failed case in post-merge | EmmaQiaoCh | +4/-0 (2 files) | 1.9h | - |
| #5569 | test: [CI] Add failed cases into waives.txt | xinhe-nv | +2/-0 (1 files) | 52.0h | - |
| #5604 | [ci] move eagle1 and medusa tests to post-merge | omera-nv | +6/-6 (1 files) | 3.6h | - |
| #5615 | [TRTLLM-5812][feat] support FP8 row-wise dense GEMM in torch... | DylanChen-NV | +455/-6 (9 files) | 164.3h | - |
| #5616 | [TRTLLM-5826][feat] Support pytorch LoRA adapter eviction | amitz-nv | +457/-131 (14 files) | 470.0h | - |
| #5634 | [fix] Update to properly set cuda graphs in trtllm-bench ove... | FrankD412 | +12/-14 (1 files) | 87.5h | - |
| #5638 | doc: Fix outdated config in DeepSeek best perf practice doc | kaiyux | +36/-38 (1 files) | 0.4h | - |
| #5654 | test: Validate and add accuracy& perf tests for Ministral-8B... | venkywonka | +58/-7 (6 files) | 170.8h | - |
| #5674 | [Infra] - Waive failed cases on release/0.21 | EmmaQiaoCh | +2/-0 (2 files) | 15.9h | - |
| #5705 | [https://nvbugs/5365714] fix(scaffolding): use default LLM r... | dc3671 | +1/-2 (1 files) | 5.2h | Scaffolding |
| #5706 | chore [TRTLLM-6161]: add LLM speculative decoding example | Superjomn | +127/-0 (3 files) | 133.8h | - |
| #5724 | Cherry pick "[NVBUG:5355009] Modify check for fuse_fp4_quant... | farazkh80 | +2/-5 (2 files) | 13.8h | - |
| #5740 | Waive tests : test_openai_lora, test_trtllm_serve_lora_examp... | venkywonka | +3/-0 (1 files) | 0.7h | - |
| #5745 | Add dummy all_reduce for kernel breakdown | qiaoxj07 | +22/-0 (1 files) | 24.8h | - |
| #5747 | Update transformers to 4.53.0 | Wanli-Jiang | +66/-40 (10 files) | 132.3h | - |
| #5776 | cherry pick #5416 | QiJune | +3/-2 (1 files) | 7.2h | - |
| #5782 | [NvBug 5362426] fix: Fix prompt adapter TP2 case | syuoni | +16/-8 (2 files) | 27.2h | - |
| #5789 | [nvbugs/5326453] Avoid nesting NCCL grouping in allgather OP | QiJune | +54/-61 (5 files) | 22.1h | - |
| #5804 | [TRTLLM-6081] doc: KV cache feature documentation | thorjohnsen | +75/-1 (1 files) | 1244.5h | - |
| #5821 | fix: [https://nvbugs/5351130][https://nvbugs/5333654] Unwaiv... | bobboli | +0/-2 (1 files) | 6.9h | - |
| #5840 | doc: Update gb200 doc | yizhang-nv | +1/-0 (1 files) | 1.4h | - |
| #5865 | [https://nvbugs/5355316] fix: update torch.compile option to... | dc3671 | +2/-2 (2 files) | 25.3h | - |
| #5868 | Fix: Enhance ModelConfig for kv cache size calculations | qixiang-99 | +58/-9 (6 files) | 186.4h | - |
| #5885 | [TRTLLM-6264] Fix flaky test_e2e.py::test_openai_lora | thorjohnsen | +14/-4 (2 files) | 54.8h | - |
| #5906 | tests: update sanity tests & fix tests | xinhe-nv | +360/-453 (4 files) | 26.4h | - |
| #5919 | Feat: Add vectorized loading for finalize kernel in MoE Trtl... | ChristinaZ | +106/-4 (1 files) | 158.1h | - |
| #5926 | [nvbugs/5354884][fix] Update beam search workspace estimatio... | stnie | +13/-3 (1 files) | 192.4h | - |
| #5931 | [fix] Remove SpecConfig and fix thread leak issues | mikeiovine | +15/-24 (5 files) | 40.0h | - |
| #5994 | chore: set default device to cpu on Multimodal models | yechank-nvidia | +23/-36 (5 files) | 214.8h | - |
| #5997 | [TRTLLM-5271][feat] best_of/n for pytorch workflow | evezhier | +332/-56 (9 files) | 507.2h | - |
| #6003 | chore: [Breaking Change] Rename cuda_graph_config padding_en... | nv-guomingz | +156/-139 (29 files) | 19.1h | - |
| #6024 | doc: Adding disaggregated serving page to features section f... | pcastonguay | +260/-1 (1 files) | 360.3h | - |
| #6027 | GEMM+AR TP2 harness fix | xavier-nvidia | +1/-1 (1 files) | 0.2h | - |
| #6041 | [nvbug/5347489][nvbug/5388036] increase timeout in disagg wo... | zhengd-nv | +15/-10 (1 files) | 23.4h | - |
| #6082 | [None] - Waive L0 tests | yiqingy0 | +2/-0 (1 files) | 2.3h | - |
| #6086 | chore: Bump version to 1.0.0rc4 | yiqingy0 | +3/-3 (3 files) | 0.4h | - |
| #6097 | [TRTLLM-1302][feat] Topk logprobs for TRT backend and top1 l... | LinPoly | +222/-125 (11 files) | 1385.7h | - |
| #6101 | test: update max_beam_width to 1 due to torchsampler changes... | nv-guomingz | +3/-3 (1 files) | 17.3h | - |
| #6139 | [TRTLLM-6537][infra] extend multi-gpu tests related file lis... | reasonsolo | +38/-37 (1 files) | 119.5h | - |
| #6147 | [nvbug/5393888][nvbug/5393042] Always use `py_seq_slot` | netanel-haber | +16/-16 (3 files) | 28.0h | - |
| #6161 | [Doc][Qwen3] update qwen3 into support-matrix | byshiue | +3/-1 (1 files) | 5.2h | Doc |
| #6176 | [Infra] - Waive failed tests in post-merge | EmmaQiaoCh | +11/-0 (2 files) | 0.5h | - |
| #6181 | [https://nvbugs/5393961][fix] record kv-cache size in MLACac... | bo-nv | +4/-0 (1 files) | 11.6h | - |
| #6223 | [TRTLLM-6651][feat]  Enable Overlap scheduler +  Beam Search... | stnie | +107/-27 (3 files) | 42.3h | - |
| #6262 | [https://nvbugs/5387771] fix deadlocks due to insufficient n... | PerkzZheng | +8/-1 (2 files) | 11.8h | - |
| #6263 | [TRTLLM-6654][feat] Add support for external multimodal embe... | chang-l | +506/-26 (7 files) | 189.8h | - |
| #6333 | test: [CI] Add failed cases into waives.txt | xinhe-nv | +18/-4 (5 files) | 16.8h | - |
| #6338 | [fix] Add trust_remote_code option to prepare_dataset. | FrankD412 | +18/-9 (1 files) | 98.9h | - |
| #6386 | [None][infra] Enable accuracy test for eagle3 and chunked pr... | leslie-fang25 | +12/-5 (3 files) | 170.5h | Community want to contribute |
| #6390 | tests: add TestNemotronH cuda graph tests | xinhe-nv | +114/-7 (4 files) | 51.9h | - |
| #6466 | test: Add time logging for lora tests | brb-nv | +55/-3 (5 files) | 18.3h | - |
| #6472 | [None][fix] fix: resolve GPU memory imbalance in concurrent ... | Nekofish-L | +22/-3 (3 files) | 3536.2h | Community want to contribute |
| #6494 | [TRTLLM-6812][feat] Add standardized GitHub issue templates ... | venkywonka | +568/-114 (10 files) | 283.8h | - |
| #6537 | [https://nvbugs/5394392][fix] Enlarge scheduler capacity und... | yifeizhang-c | +83/-2 (7 files) | 349.2h | - |
| #6548 | [None][feat] improve dataloading for benchmark_dataset by us... | zerollzeng | +321/-74 (1 files) | 234.0h | - |
| #6555 | [TRTLLM-6893][infra] fix Build Docker Image tag issue | ZhanruiSunCh | +8/-10 (1 files) | 94.6h | - |
| #6563 | [TRTLLM-6881][feat] Include attention dp rank info with KV c... | pcastonguay | +835/-73 (22 files) | 138.8h | - |
| #6590 | [None][chore] add missing tests to test list | Superjomn | +8/-1 (2 files) | 57.0h | Release Blocker |
| #6592 | [TRTLLM-6823][doc] Add checkpoint refactor docs | shaharmor98 | +335/-3 (3 files) | 162.2h | - |
| #6597 | [None][chore] Bump version to 1.0.0rc6 | yiqingy0 | +3/-3 (3 files) | 0.4h | - |
| #6651 | [None][chore] Bump version to 1.1.0rc0 | yiqingy0 | +3/-3 (3 files) | 26.1h | - |
| #6657 | [None][chore] optimize kv cache transfer for context TEP and... | chuangz0 | +24/-13 (3 files) | 20.8h | - |
| #6660 | [https://nvbugs/5409414][fix] fix Not registered specs | xinhe-nv | +12/-4 (7 files) | 23.4h | - |
| #6698 | [TRTLLM-6853][feat] refactor deepseekv3 model | kris1025 | +100/-107 (5 files) | 173.9h | - |
| #6699 | [https://nvbugs/5429689][fix] Fix mllama model structure upd... | dominicshanshan | +12/-2 (1 files) | 89.4h | - |
| #6704 | [TRTLLM-6854][feat] Enable guided decoding with disagg servi... | syuoni | +175/-24 (7 files) | 17.4h | - |
| #6714 | [https://nvbugs/5394409][feat] Support Mistral Small 3.1 mul... | dbari | +821/-80 (28 files) | 336.7h | - |
| #6724 | [None][doc] add legacy section for tensorrt engine | Superjomn | +68/-7 (7 files) | 171.3h | - |
| #6739 | [None][doc] Add doc for multimodal feature support matrix (#... | nv-guomingz | +13/-0 (1 files) | 0.6h | - |
| #6744 | [https://nvbugs/5444624][fix] Fix LLM_ROOT in triton_backend... | yiqingy0 | +2/-1 (1 files) | 67.8h | - |
| #6750 | [TRTLLM-6633][feat] Padding for piecewise cudagraph | liji-nv | +324/-218 (10 files) | 444.6h | - |
| #6762 | [TRTLLM-7025] [infra] Reorganize CODEOWNERS to rectify `exam... | venkywonka | +28/-23 (1 files) | 2.9h | - |
| #6763 | [None][chore] Find LLM_ROOT and LLM_BACKEND_ROOT dynamically | achartier | +45/-33 (2 files) | 72.5h | - |
| #6775 | [None][feat] Enable gpt oss on DGX H100. | Tracin | +4/-0 (2 files) | 1045.0h | - |
| #6791 | [None][infra] Unwaive an updated case to test | EmmaQiaoCh | +0/-1 (1 files) | 1.1h | - |
| #6794 | [None] [feat] Enable run_post_quant_allgather for MoE TRTLLM... | ChristinaZ | +1697/-772 (28 files) | 1021.6h | - |
| #6796 | [None] [chore] Mamba cache in separate file | tomeras91 | +250/-225 (4 files) | 93.9h | - |
| #6825 | [None][fix] Fix python-only build that uses TRTLLM_USE_PRECO... | jiaganc | +10/-9 (2 files) | 53.3h | - |
| #6873 | [https://nvbugs/5455651][fix] Make ngram use XQA attention o... | mikeiovine | +7/-5 (1 files) | 25.8h | - |
| #6908 | [None][doc] Update gpt-oss doc on MoE support matrix | hlu1 | +10/-6 (1 files) | 6.4h | - |
| #6944 | [None][chore] unwaive test_disaggregated_genbs1 | bo-nv | +0/-1 (1 files) | 112.7h | - |
| #6945 | [None][infra] update feature_combination_matrix of disaggreg... | leslie-fang25 | +8/-5 (3 files) | 63.5h | - |
| #6984 | [https://nvbugs/5453827][fix] Fix RPATH of th_common shared ... | tongyuantongyu | +4/-10 (3 files) | 73.0h | - |
| #6990 | [https://nvbugs/5450074][fix] Reduce the device memory requi... | Shixiaowei02 | +4/-2 (2 files) | 96.2h | - |
| #6996 | [https://nvbugs/5458874][fix] Fix Nemotron-H flaky CUDA grap... | tomeras91 | +14/-4 (1 files) | 24.2h | - |
| #7008 | [https://nvbugs/5462007][ci] Unwaive Mistral Small 3.1 FP8 t... | 2ez4bz | +0/-1 (1 files) | 5.3h | - |
| #7013 | [None][feat] Skip prefetching consolidated safetensors when ... | 2ez4bz | +95/-0 (4 files) | 173.1h | - |
| #7041 | [TRTLLM-7153] [feat] Move stop_criteria to sample_async | netanel-haber | +633/-139 (5 files) | 458.1h | - |
| #7143 | [TRTLLM-7321][doc] Add GPT-OSS Deployment Guide into officia... | dongfengy | +329/-0 (2 files) | 9.0h | - |
| #7171 | [None][chore] Mass integration of release/1.0 - 2nd | dominicshanshan | +891/-611 (38 files) | 228.6h | - |
| #7173 | [https://nvbugs/5467062][fix] pass logitsPostProcessorBatche... | brb-nv | +86/-29 (22 files) | 79.1h | - |
| #7179 | [None][chore] Enable auto deploy accuracy test in CI | ajrasane | +10/-3 (6 files) | 41.2h | - |
| #7210 | [None][fix] fix log_once usage | yuxianq | +4/-2 (3 files) | 25.2h | - |
| #7211 | [None][test] add kv cache size in bench metric and fix faile... | ruodil | +19/-23 (3 files) | 16.1h | - |
| #7233 | [None][doc] Update autodeploy README.md, deprecate lm_eval i... | Fridah-nv | +19/-656 (4 files) | 18.0h | - |
| #7238 | [None][fix] Remove and fuse some element-wise ops in the ds-... | lfr-0531 | +82/-50 (4 files) | 23.4h | - |
| #7252 | [None][docs] refine docs for accuracy evaluation of gpt-oss ... | binghanc | +22/-0 (1 files) | 305.7h | Community want to contribute, waiting for feedback |
| #7258 | [None][infra] Waive failed cases for release/1.0 08/26 | EmmaQiaoCh | +1/-0 (1 files) | 1.0h | - |
| #7277 | [TRTLLM-7408][feat] Wrap MOE with custom op. | liji-nv | +272/-118 (17 files) | 325.6h | - |
| #7286 | [https://nvbugs/5378031] [feat] W4A8 AWQ MoE supports Per Ex... | yumin066 | +217/-72 (7 files) | 1195.2h | - |
| #7333 | [None][ci] skip TestGPTOSS | QiJune | +4/-2 (1 files) | 0.9h | - |
| #7360 | [TRTLLM-7410][feat] Support hashing and KV cache reuse for v... | chang-l | +323/-84 (6 files) | 157.5h | - |
| #7362 | [None][doc] update architecture overview doc | QiJune | +14/-1 (2 files) | 1.2h | - |
| #7366 | [https://nvbugs/5485593][fix] improve accuracy/test_disaggre... | reasonsolo | +32/-20 (1 files) | 125.9h | - |
| #7409 | [None] [fix] Fix nsys in slurm scripts | kaiyux | +5/-4 (2 files) | 8.9h | - |
| #7413 | [TRTLLM-6643][feat] Add DeepSeek-v3-0324 e2e torch test | aalanwyr | +9/-1 (3 files) | 30.3h | - |
| #7421 | [None][test] auto reuse torch empty cache on qa test | crazydemo | +1/-2 (2 files) | 26.8h | - |
| #7505 | [https://nvbugs/5494698][fix] skip gemma3 27b on blackwell | xinhe-nv | +22/-13 (5 files) | 171.4h | - |
| #7534 | [None][fix] Update DG commit | Barry-Delaney | +1/-1 (1 files) | 3.9h | - |
| #7563 | [TRTLLM-7918][feat] Support kvcache reuse for phi4mm | Wanli-Jiang | +25/-7 (3 files) | 238.3h | - |
| #7568 | [TRTLLM-4629] [feat] Add support of CUDA13 and sm103 devices | VALLIS-NERIA | +1112/-511 (97 files) | 249.7h | - |
| #7598 | [None][chore] Make use_low_precision_moe_combine as a llm ar... | zongfeijing | +21/-4 (6 files) | 18.0h | - |
| #7607 | [None][chore] Mass integration of release/1.0 - 4th (release... | dominicshanshan | +4597/-590 (79 files) | 20.5h | - |
| #7628 | [TRTLLM-7410][feat] Enable KV cache reuse and chunked prefil... | 2ez4bz | +172/-61 (6 files) | 210.1h | - |
| #7635 | [#7308] [feat] AutoDeploy: graph-less transformers mode for ... | lucaslie | +1280/-223 (28 files) | 213.0h | - |
| #7696 | [None][doc] Add labels description note into llm api section | nv-guomingz | +8/-1 (1 files) | 26.0h | Release Blocker |
| #7720 | [None][fix] waive hang tests on main | xinhe-nv | +4/-0 (1 files) | 24.3h | - |
| #7723 | [TRTLLM-7918][feat] Support kvcache reuse and chunk prefill ... | Wanli-Jiang | +86/-20 (5 files) | 71.8h | - |
| #7724 | [https://nvbugs/5355219][fix] Fix trtllm moe backend  test c... | yizhang-nv | +17/-7 (6 files) | 16.6h | - |
| #7757 | [TRTLLM-6286] [perf] Add NoSmem epilogue schedule and dynami... | VALLIS-NERIA | +256/-153 (12 files) | 115.7h | - |
| #7770 | [#5860][feat] Add ModelOPT INT4 awq fake quant support in Au... | Fridah-nv | +369/-3 (7 files) | 363.8h | - |
| #7837 | [None][doc] Replace the main in the examples' link with comm... | nv-guomingz | +6/-3 (1 files) | 5.2h | - |
| #7841 | [None][chore] Add failed cases into waives.txt | xinhe-nv | +15/-42 (4 files) | 19.8h | - |
| #7893 | [TRTLLM-8209][feat] Support new structural tag API (upgrade ... | syuoni | +42/-62 (7 files) | 20.4h | - |
| #7917 | [None] [feat] Update disagg gen-only benchmark. | qiaoxj07 | +31/-8 (1 files) | 120.2h | - |
| #7965 | [https://nvbugs/5451740][fix] Add DP padding back on SM120 | peaceh-nv | +8/-0 (1 files) | 38.1h | - |
| #7977 | [TRTLLM-6748][feat] add PDL support for more kernels | dc3671 | +145/-28 (9 files) | 379.3h | - |
| #8024 | [TRTLLM-8238][feat] Add EVS support for nano-v2-vlm | Wanli-Jiang | +586/-77 (4 files) | 696.2h | - |
| #8063 | [https://nvbugs/5510879][fix] Fix pytorch & TRT-python flows... | amitz-nv | +229/-78 (11 files) | 318.4h | - |
| #8081 | [TRTLLM-6239][feat] add test cases into QA test list | xinhe-nv | +4/-0 (3 files) | 2.7h | - |
| #8174 | [TRTLLM-7769][chore] document the role of 'd2t' | ixlmar | +11/-11 (1 files) | 55.1h | - |
| #8185 | [None][chore] Waive tests failing on release/1.1 post merge | brb-nv | +8/-0 (1 files) | 15.7h | - |
| #8206 | [https://nvbugs/5563469][fix] Temporarily disable test_nemot... | moraxu | +2/-1 (1 files) | 135.7h | - |
| #8212 | [TRTLLM-8246][test] add multimodal kvcache+chunked_prefil ca... | crazydemo | +12/-0 (2 files) | 94.3h | - |
| #8230 | [None][infra] Waive failed tests on main 10/09 | EmmaQiaoCh | +2/-0 (2 files) | 0.9h | - |
| #8261 | [None][feat] Add torch compile support for cuda core GEMM OP | DylanChen-NV | +15/-0 (1 files) | 67.3h | - |
| #8294 | [https://nvbugs/5404000][fix] Ensure consistency between fir... | achartier | +2/-2 (1 files) | 41.1h | - |
| #8302 | [TRTLLM-8511][feat] Add update_weights and sleep_wakeup supp... | shuyixiong | +852/-185 (23 files) | 540.8h | - |
| #8307 | [https://nvbugs/5550671][fix] fix disagg-serving multinodes ... | reasonsolo | +21/-11 (2 files) | 23.0h | - |
| #8319 | [TRTLLM-8435][infra] Test existing rtxpro6000 stages on rtxp... | EmmaQiaoCh | +23/-6 (2 files) | 507.0h | - |
| #8321 | [None][test] Add post merge test for Seed-OSS-36B-Instruct | zhhuang-nv | +109/-15 (9 files) | 93.3h | - |
| #8322 | [https://nvbugs/5537738][fix] Add fp8 post-quant allgather s... | ChristinaZ | +18/-11 (2 files) | 1285.1h | - |
| #8323 | [None] [blog] Scaling Expert Parallelism in TensorRT LLM (Pa... | kaiyux | +239/-0 (9 files) | 0.5h | - |
| #8332 | [None][feat] Add FP8 rowwise GEMMs for B200 | achartier | +395/-3 (4 files) | 335.9h | - |
| #8349 | [None][ci] waive several rpc tests | Superjomn | +2/-0 (2 files) | 6.4h | - |
| #8353 | [https://nvbugs/5541494] [fix] Remove waivers | VALLIS-NERIA | +0/-3 (1 files) | 44.3h | - |
| #8392 | [None][feat] Add fmha_v2 kernel for head_dim=80 and sm=100 t... | Wanli-Jiang | +14/-1 (2 files) | 51.0h | - |
| #8437 | [https://nvbugs/5568676][fix] Remove test waive | dongfengy | +0/-1 (1 files) | 97.7h | - |
| #8440 | [https://nvbugs/5515753][ci] Add NCCL_DEBUG=INFO flag to col... | SimengLiu-nv | +8/-4 (4 files) | 126.2h | - |
| #8509 | [TRTLLM-6756][feat] Add Beam Search to TorchSampler | stnie | +2156/-462 (10 files) | 1009.3h | - |
| #8523 | [TRTLLM-7835][test] add default sample config for perf test | ruodil | +44/-2 (2 files) | 167.2h | - |
| #8534 | [None][chore] add precommit hook to remove redundant tab and... | xinhe-nv | +55/-2 (3 files) | 26.1h | - |
| #8561 | [TRTLLM-8817][chore] Set default value of KvCacheConfig.free... | QiJune | +15/-18 (6 files) | 45.5h | - |
| #8585 | [None][infra] Fix slurm exitcode | EmmaQiaoCh | +0/-4 (1 files) | 24.2h | - |
| #8600 | [TRTLLM-8836][chore] Create ModelEngine from LlmArgs | QiJune | +160/-181 (9 files) | 226.1h | - |
| #8601 | [None] [test] Add MNNVL AlltoAll tests to pre-merge | kaiyux | +41/-20 (6 files) | 106.8h | - |
| #8611 | [https://nvbugs/5587456][fix] Remove multimodal test cases u... | jieli-matrix | +0/-10 (1 files) | 27.9h | - |
| #8625 | [https://nvbugs/5593199][test] Enhance beam search tests det... | stnie | +388/-91 (1 files) | 138.9h | - |
| #8657 | [None][autodeploy] minor refactor to rmsnorm transforms | Fridah-nv | +62/-78 (5 files) | 484.3h | - |
| #8665 | [None][doc] Clarify the perf best practice and supported har... | dongfengy | +5/-5 (1 files) | 139.9h | - |
| #8678 | [TRTLLM-8933][chore] remove unused update_executor_config fu... | QiJune | +19/-93 (3 files) | 7.8h | - |
| #8724 | [TRTLLM-8971][infra] Update gpu key for B300/GB300 | EmmaQiaoCh | +6/-0 (5 files) | 40.8h | - |
| #8750 | [None][fix] Fix KV cache clearing with KV Connector API | jthomson04 | +34/-10 (2 files) | 209.7h | - |
| #8776 | [None][feat] Add benchmark to DeepConf | dcaox | +320/-75 (5 files) | 99.1h | - |
| #8800 | [TRTLLM-9000][feat] Add multi-node Perf Tests into CI | chenfeiz0326 | +2113/-613 (16 files) | 922.1h | - |
| #8812 | [#8763][feature] AutoDeploy: configurable dtype for caching | lucaslie | +79/-12 (6 files) | 273.4h | - |
| #8838 | [TRTLLM-8994][infra] upgrade to DLFW 25.10 and pytorch 2.9.0... | ZhanruiSunCh | +103/-255 (22 files) | 100.5h | - |
| #8868 | [None][infra] Modify wheel path from cuda13/ to dlfw/ | ZhanruiSunCh | +2/-2 (1 files) | 5.5h | - |
| #8877 | [TRTLLM-9080][infra] upgrade tritonserver DLFW 25.10 | ZhanruiSunCh | +7/-8 (4 files) | 164.9h | - |
| #8913 | [None][feat] add swapsMmaAb sparseMla kernels | PerkzZheng | +4656/-4362 (1503 files) | 27.5h | - |
| #8970 | [https://nvbugs/5633340][fix] kill processes properly after ... | reasonsolo | +7/-8 (2 files) | 20.8h | - |
| #8987 | [None][infra] Update allowed list 2025.11.06 | yuanjingx87 | +292/-2 (1 files) | 21.2h | - |
| #9126 | [None] [fix] Disable UCC as WAR to MPI allgather issue befor... | kaiyux | +5/-1 (1 files) | 4.0h | Release Blocker |
| #9145 | [https://nvbugs/5647400] [fix] Enlarged the AllReduce worksp... | MrGeva | +585/-73 (15 files) | 290.9h | - |
| #9171 | [None] [fix] Fix missing ActivationType issue | kaiyux | +35/-26 (10 files) | 67.0h | - |
| #9195 | [None][feature] AutoDeploy: tighter MoE UT thresholds | nzmora-nvidia | +29/-12 (1 files) | 73.5h | - |
| #9201 | [https://nvbugs/5649826][fix] Unwaive test test_llm_commandr... | sunnyqgg | +2/-2 (1 files) | 4.9h | - |
| #9204 | [None] [tests] Unwaive wide ep related tests | kaiyux | +0/-8 (1 files) | 37.3h | - |
| #9206 | [https://nvbugs/5652552][fix] cherry-pick add printing for l... | ruodil | +2/-1 (1 files) | 385.9h | - |
| #9209 | [None][ci] split speculative test case into several small ca... | QiJune | +2/-1 (1 files) | 17.3h | - |
| #9290 | [None][infra] Add fallback when get wheel from build stage i... | ZhanruiSunCh | +30/-11 (1 files) | 50.6h | - |
| #9348 | [TRTLLM-7963][fix] Several improvements of autotuning qualit... | hyukn | +59/-39 (2 files) | 71.8h | - |
| #9491 | [None][fix] Correct virtual memory allocation alignment | tongyuantongyu | +79/-10 (3 files) | 113.4h | - |
| #9506 | [https://nvbugs/5422621][test] Add GB 200 WIDEEP test case f... | fredricz-20070104 | +435/-4 (49 files) | 264.4h | - |
| #9534 | [None][chore] remove qwen3-next accuracy tests | JadoTu | +1/-15 (4 files) | 70.4h | - |
| #9544 | [None][feat] add chat template kwargs support to longbench-v... | lfr-0531 | +18/-4 (1 files) | 68.9h | - |
| #9610 | [#9432][fix] Resolve NameError in memory profiler for v0.12.... | bonginn | +8/-0 (1 files) | 354.3h | Community want to contribute |
| #9620 | [None][infra] Remove an invalid test name in waives.txt | EmmaQiaoCh | +1/-1 (1 files) | 1.8h | - |
| #9622 | [https://nvbugs/5561153][test] Fix log error for perf test | fredricz-20070104 | +39/-31 (1 files) | 22.3h | - |
| #9769 | [None][infra] Waive failed cases for main branch on 12/07 | EmmaQiaoCh | +5/-0 (1 files) | 2.3h | - |
| #9812 | [https://nvbugs/5597647][ci] Unwaive fixed tests. | SimengLiu-nv | +0/-1 (1 files) | 67.3h | - |
| #9833 | [TRTLLM-9262][test] add groupgemm ada case for rcca | crazydemo | +4/-1 (2 files) | 69.9h | - |
| #9836 | [#9640][feat] Migrate model registry to v2.0 format with com... | tcherckez-nvidia | +472/-0 (17 files) | 245.5h | - |
| #9849 | [None][doc] Adding parallelism types in feature combination ... | pcastonguay | +21/-17 (1 files) | 694.9h | - |
| #9876 | [None][ci] Move remaining DGX-B200 tests to LBD | chzblych | +69/-46 (6 files) | 422.8h | - |
| #9885 | [None][feat] Implement sampling on 1-model EAGLE3 | mikeiovine | +248/-5 (9 files) | 65.8h | - |
| #9896 | [https://nvbugs/5727481][ci] Fix Port Conflict in Perf-Sanit... | chenfeiz0326 | +198/-154 (9 files) | 26.1h | - |
| #9910 | [#9717][chore] Refactor MoE code to use enums | tcherckez-nvidia | +246/-246 (13 files) | 273.6h | - |
| #9984 | [TRTLLM-9565][fix] Fix deepseek sharding | greg-kwasniewski1 | +419/-351 (4 files) | 210.6h | - |
| #9986 | [TRTLLM-9493][feat] Custom AllToAll for helix parallelism | brb-nv | +1242/-107 (14 files) | 220.0h | - |
| #9996 | [None][infra] Add multi gpu Ray tests into L0 merge change r... | dominicshanshan | +3/-0 (1 files) | 1.9h | - |
| #10005 | [TRTC-102][docs] `--extra_llm_api_options`->`--config` in do... | venkywonka | +625/-498 (70 files) | 104.9h | - |
| #10040 | [TRTLLM-9989][fix] Disable tvm_ffi for CuteDSL nvFP4 dense G... | hyukn | +3/-3 (1 files) | 23.8h | - |
| #10043 | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overl... | syuoni | +259/-183 (14 files) | 93.6h | - |
| #10055 | [None][infra] Move install_boost from install_triton.sh to i... | Tabrizian | +21/-20 (3 files) | 211.4h | - |
| #10060 | [https://nvbugs/5717993][fix] Add execution_stream across Py... | SimengLiu-nv | +321/-36 (12 files) | 357.8h | - |
| #10062 | [https://nvbugs/5729697][fix] MNNVL Allreduce: use CUDA runt... | timlee0212 | +63/-63 (2 files) | 153.9h | - |
| #10082 | [TRTLLM-9455][feat] support for new checkpoint | binghanc | +156/-16 (1 files) | 308.6h | Community want to contribute |
| #10125 | [TRTC-121] [feat] Add recipe selector UI to complement the r... | venkywonka | +1124/-71 (11 files) | 159.9h | - |
| #10135 | [https://nvbugs/5747911][fix] Use offline data path for the ... | chang-l | +3/-2 (2 files) | 3.8h | - |
| #10215 | [https://nvbugs/5622938][feat] Run sample_async on extra str... | yuxianq | +22/-2 (1 files) | 412.3h | Decoding/Sampling |
| #10256 | [None][feat] Drop non-deepgemm fp8 block scale gemm | lucifer1004 | +9/-973 (3 files) | 27.8h | - |
| #10271 | [https://nvbugs/5766986][fix] fixed the shard_all_unprocesse... | MrGeva | +1/-11 (2 files) | 148.8h | - |
| #10284 | [None][feat] Speculative One Model: FlashInfer sampling | IzzyPutterman | +23/-1 (2 files) | 645.4h | - |
| #10293 | [None][ci] Waive TestLlama3_1_8B::test_auto_dtype[False-2] f... | syuoni | +1/-0 (1 files) | 0.8h | - |
| #10301 | [None][chore] Add failed cases into waives.txt | xinhe-nv | +3/-1 (1 files) | 109.2h | - |
| #10386 | [https://nvbugs/5772521][fix] Fix draft token tree chain cra... | mikeiovine | +3/-4 (1 files) | 68.9h | - |
| #10429 | [None] [feat] Add test script and raster M for gather fc1 ke... | zongfeijing | +1555/-31 (3 files) | 22.8h | - |
| #10442 | [None][test] restrict max_num_tokens in disagg mtp config | ruodil | +30/-17 (17 files) | 66.9h | - |
| #10444 | [https://nvbugs/5701445][chore] isolate test. | yuxianq | +1/-1 (1 files) | 233.4h | - |
| #10451 | [https://nvbugs/5753788][chore] Padding empty chunk for conf... | leslie-fang25 | +22/-1 (1 files) | 185.1h | - |
| #10489 | [TRTLLM-10248][feat] Support Bot to Send Perf Regression Msg... | chenfeiz0326 | +530/-142 (7 files) | 118.7h | - |
| #10499 | [https://nvbugs/5788127][fix] Use uint64_t as the dtype of l... | yilin-void | +55/-38 (5 files) | 143.1h | - |
| #10500 | [None] [feat] Support multiple accuracy tasks for slurm scri... | kaiyux | +190/-100 (8 files) | 213.5h | - |
| #10516 | [https://nvbugs/5628848][fix] Fix nanobind stub generation | Linda-Stadter | +1/-1 (2 files) | 49.2h | - |
| #10561 | [None][feat] Add support for DeepSeek v3.2 tests | yingguo-trt | +62/-38 (6 files) | 13.1h | - |
| #10597 | [None][chore] Print correct backend name in benchmark report | galagam | +1/-1 (1 files) | 13.1h | - |
| #10629 | [None][test] add log_samples and output_path for trtllm_eval | dc3671 | +83/-7 (2 files) | 22.8h | - |
| #10660 | [https://nvbugs/5794313][chore] unwaive tests. | yuxianq | +0/-1 (1 files) | 70.4h | - |
| #10691 | [TRTLLM-9111][feat] MoE test refactor: Extend MoE quantizati... | xxi-nv | +1120/-86 (1 files) | 19.6h | - |
| #10727 | [None][fix] AutoDeploy: Fix the nvfp4 fused_moe | nvchenghaoz | +266/-26 (6 files) | 22.8h | - |
| #10779 | [None][test] modify ctx config in 128k8k disagg cases | ruodil | +60/-59 (35 files) | 18.9h | - |
| #10792 | [None][chore] switch to ConfigurableMoE as the default path | xxi-nv | +9/-24 (5 files) | 52.3h | - |
| #10793 | [https://nvbugs/5814253][fix] unwaive test_autotuner_distrib... | hyukn | +1/-3 (2 files) | 51.8h | - |
| #10870 | [None][chore] Revert NVIDIA/TensorRT-LLM#10819 | chzblych | +2/-2 (1 files) | 0.3h | - |


---

## 二、被阻塞的PR列表 (87个)

这些PR至少经历了一次打回或阻塞。

| PR编号 | 标题 | 提交者 | 卡点类型 | 代码变更 | 合并耗时 |
|-------|------|--------|---------|---------|---------|
| #4804 | [fix] Do not reuse dummy request KVCache | liji-nv | Review(1x) | +19/-3 | 308.2h |
| #4936 | Raise shut down error for each request | Shunkangz | Review(1x) | +25/-4 | 698.8h |
| #4962 | [TRTLLM-6088][doc] Add speculative decoding PyTorc... | mikeiovine | Precommit | +249/-2 | 938.2h |
| #5234 | chore:[BREAKING CHANGE] use cacheTransceiverConfig... | chuangz0 | Review(1x) | +600/-265 | 746.6h |
| #5333 | [TRTLLM-3442] feat: added beam search support to t... | stnie | Review(2x) | +423/-123 | 387.2h |
| #5662 | add supported models doc | QiJune | Precommit | +38/-2 | 121.9h |
| #5667 | [Infra] - Set default timeout to 1hr and remove so... | EmmaQiaoCh | CI | +30/-30 | 3.8h |
| #5771 | Refactor the rest routing part for the routing ker... | ChristinaZ | Review(1x) | +2444/-3602 | 113.0h |
| #5995 | [None][doc]: remove the outdated features which ma... | nv-guomingz | Title | +18/-32 | 569.5h |
| #6090 | [None][chore] ucx establish connection with zmq | chuangz0 | Title | +206/-38 | 479.7h |
| #6146 | [fix]: Skip prompt length checking for generation ... | LinPoly | Review(1x) | +21/-9 | 48.1h |
| #6542 | [None][feat] Add test for speculative rejection sa... | IzzyPutterman | Title | +209/-79 | 308.6h |
| #6701 | [https://nvbugs/5441438][fix] Set correct draft le... | ziyixiong-nv | Review(1x) | +51/-28 | 111.7h |
| #6896 | [https://nvbugs/5394685][fix] using static schedul... | PerkzZheng | Title | +27/-11 | 17.2h |
| #6940 | [https://nvbugs/5448437][fix] fix some nixl tests | bo-nv | Title | +10/-11 | 118.2h |
| #7003 | [None][fix] Fix build of tritonbuild/tritonrelease... | dbari | Review(1x) | +26/-15 | 47.8h |
| #7004 | [https://nvbugs/5444937][chore] Fixing KV events t... | pcastonguay | Title | +30/-28 | 23.9h |
| #7070 | [None][fix] fix scaffolding dynasor test | dc3671 | Title | +16/-20 | 4.1h |
| #7232 | [None][feat] Add logging for OAI disagg server | Tabrizian | Review(1x) | +71/-11 | 28.8h |
| #7358 | [None] [doc] Update DeepSeek example doc | jiahanc | Checklist | +78/-18 | 87.0h |
| #7538 | [None][fix] Fix a typo in the Slurm CI codes (#748... | chzblych | Checklist | +11/-6 | 1.6h |
| #7585 | [None][ci] Waive qwen3 test for accuracy bug in ht... | dominicshanshan | Checklist | +2/-0 | 7.2h |
| #7604 | [https://nvbugs/5506683][fix] adjust the CI | byshiue | Checklist | +2/-2 | 0.8h |
| #7616 | [https://nvbugs/5505402] [fix] Disable deep_gemm f... | DomBrown | Checklist | +44/-21 | 53.8h |
| #7639 | [None][fix] add the missing import raised by #7607 | nv-guomingz | Checklist | +1/-1 | 0.5h |
| #7678 | [None][test] add test for min_tokens | ixlmar | Checklist | +19/-0 | 112.2h |
| #7686 | [https://nvbugs/5471108][chore] Unwaiving disagg a... | pcastonguay | Checklist | +0/-2 | 208.0h |
| #7808 | [https://nvbugs/5513423][fix] Correctly respect mi... | stnie | Checklist | +56/-8 | 112.0h |
| #7877 | [https://nvbugs/5477359][fix] Removing test waiver... | Linda-Stadter | Checklist | +0/-4 | 71.9h |
| #7900 | [https://nvbugs/5351244][fix] CHERRY-PICK test_mpi... | Superjomn | Checklist | +4/-2 | 4.9h |
| #7951 | [TRTLLM-7999][infra] Add B300/GB300 single gpu tes... | yiqingy0 | Checklist | +38/-0 | 42.5h |
| #8010 | [None][ci] Waive test_mm_encoder_standalone.py::te... | QiJune | Title, Checklist | +1/-0 | 1.1h |
| #8059 | [None][fix] Fix TRT-python multi LoRA TP=2 test ar... | amitz-nv | Checklist | +2/-0 | 7.3h |
| #8099 | [#7588][feat] lock gpu clocks in test_perf.py to r... | MrGeva | Title | +154/-3 | 44.6h |
| #8112 | [None][fix] fix patchelf version issue | bo-nv | Checklist | +1/-1 | 6.7h |
| #8167 | [https://nvbugs/5503138] [fix] Remove compile warn... | VALLIS-NERIA | Checklist | +12/-12 | 145.7h |
| #8266 | [None][infra] Remove WAR code for GH200 node | ZhanruiSunCh | Checklist | +1/-11 | 41.6h |
| #8267 | [None][infra] Remove WAR code for GH200 node | ZhanruiSunCh | Checklist | +1/-11 | 41.6h |
| #8289 | [None][chore] Update disagg benchmark configs | qiaoxj07 | Title, Checklist | +11/-6 | 25.6h |
| #8327 | [None][fix] workaround for numexpr issue | ixlmar | Checklist | +3/-0 | 3.3h |
| #8344 | [https://nvbugs/5534705][fix] Skip unnecessary CUD... | ziyixiong-nv | Checklist | +20/-13 | 49.4h |
| #8355 | [None][fix] Fix is_post_quant_all2all_supported fo... | yuantailing | Checklist | +1/-1 | 11.4h |
| #8408 | [None][chore] Isolate several intermittent cases | HuiGao-NV | Checklist | +6/-6 | 4.3h |
| #8546 | [https://nvbugs/5576192][fix] Unwaive the test for... | zheyuf | Checklist | +0/-3 | 53.2h |
| #8613 | [None][infra] Disable rtxpro6000 stages due to nod... | EmmaQiaoCh | Checklist | +4/-3 | 8.2h |
| #8668 | [None][infra] Waive failed case on main 10/26 | EmmaQiaoCh | Checklist | +1/-0 | 8.5h |
| #8728 | [None][feat] Integrate MnnvlThroughput into TRTLLM... | bobboli | Checklist | +736/-648 | 169.7h |
| #8759 | [None][infra] Waive failed tests on main 10/29 | EmmaQiaoCh | Checklist | +8/-0 | 0.9h |
| #8869 | [TRTLLM-9073/9087][doc] Add the missing content fo... | nv-guomingz | Title | +7/-2 | 5.9h |
| #8883 | [https://nvbugs/5467531][fix] Fix moe test and wid... | liji-nv | Review(1x) | +61/-35 | 63.1h |
| #8901 | [https://nvbugs/5630700][chore] Unwaive Qwen3_235B... | shuyixiong | Title, Checklist | +0/-1 | 49.1h |
| #8914 | [None][fix] Remove duplicated test waives | chzblych | Checklist | +0/-1 | 0.1h |
| #8950 | [None][perf] Adjust select_alltoall_method_type. | bobboli | Checklist | +62/-48 | 335.0h |
| #9001 | [https://nvbugs/5637037][fix] Update unwaive list. | bobboli | Checklist | +1/-1 | 65.2h |
| #9033 | [TRTLLM-9073][doc] Add the missing content for mod... | nv-guomingz | Title, Checklist | +3/-3 | 2.4h |
| #9063 | [TRTLLM-9018][infra] add mirror for Build-Docker-I... | ZhanruiSunCh | Checklist | +0/-5 | 20.5h |
| #9084 | [None][infra] Lock generation pipeline update | yuanjingx87 | Title, Checklist | +28/-1 | 59.9h |
| #9122 | [None][chore] Add placement test for ray executor | hchings | Checklist | +58/-3 | 49.8h |
| #9210 | [https://nvbugs/5590408][fix] Exclude num of draft... | ziyixiong-nv | Checklist | +73/-8 | 36.8h |
| #9320 | [None][chore] Revise the description of enable_aut... | hyukn | Checklist | +2/-1 | 5.2h |
| #9336 | [https://nvbugs/5676748][fix] Fix mismatched nvfp4... | hyukn | Checklist | +3/-3 | 91.0h |
| #9342 | [TRTLLM-5971][feat] Integrate helix parallelism | brb-nv | Review(1x) | +386/-100 | 218.6h |
| #9375 | [None][ci] waive two ray tests | Superjomn | Checklist | +2/-0 | 16.3h |
| #9435 | [https://nvbugs/5685015][fix] Update invalid max_t... | JunyiXu-nv | Checklist | +2/-1 | 68.8h |
| #9479 | [None][fix] change allreduce workspace dtype to to... | dc3671 | Checklist | +1/-1 | 27.3h |
| #9507 | [None][infra] Waive failed case in pre-merge on 11... | EmmaQiaoCh | Checklist | +1/-0 | 0.8h |
| #9539 | [None][infra] Waive failed cases for main branch o... | EmmaQiaoCh | Checklist | +12/-0 | 0.7h |
| #9559 | [None][ci] Split H100_PCIe-PyTorch-Post-Merge test... | chzblych | Checklist | +3/-3 | 0.7h |
| #9569 | [None][fix] Replace hash method with unique_id for... | hyukn | Checklist | +46/-5 | 7.4h |
| #9637 | [https://nvbugs/5705197][chore] Unwaive timeout di... | pcastonguay | Title, Checklist | +0/-5 | 17.9h |
| #9649 | [None][fix] Fix triton moe load_weight | shuyixiong | Checklist | +11/-18 | 69.4h |
| #9739 | [None][doc] Update release notes | QiJune | Review(2x) | +108/-11 | 112.4h |
| #9853 | [TRTINFRA-7328][infra] - Move half B200 tests to l... | mlefeb01 | Checklist | +2/-2 | 14.8h |
| #9887 | [None][doc] remove nano-vl-v2 model support in rel... | QiJune | Checklist | +0/-1 | 0.6h |
| #9972 | [None][doc] update readme for rpc | Superjomn | Checklist | +5/-0 | 36.1h |
| #10097 | [None][infra] Update allowlist 2025.12.17 | yuanjingx87 | Title, Checklist | +5/-0 | 5.1h |
| #10194 | [https://nvbugs/5762016][chore] Skip a ray test | shuyixiong | Checklist | +1/-0 | 0.8h |
| #10197 | [None][fix] Fix the bug for top_k=10 in NVLinkOneS... | bobboli | Checklist | +3/-3 | 21.6h |
| #10336 | [TRTLLM-10185][feat] AutoTuner Cache: Support cach... | hyukn | Checklist | +84/-49 | 141.6h |
| #10341 | [https://nvbugs/5769890][fix] Import get_free_port... | yuxianq | Checklist | +1/-5 | 14.6h |
| #10452 | [None][chore] remove redundant retries while bindi... | reasonsolo | Checklist | +7/-20 | 5.8h |
| #10466 | [https://nvbugs/5732942][fix] AutoDeploy: handle t... | lucaslie | Checklist | +93/-36 | 3.7h |
| #10670 | [None][fix] fix L0 issues | xinhe-nv | Checklist | +0/-1 | 0.1h |
| #10746 | [None][doc] update doc (add minimax model) | jmydurant | Checklist | +1/-0 | 0.9h |
| #10795 | [None][infra] Waive failed case for release branch... | EmmaQiaoCh | Checklist | +1/-0 | 0.7h |
| #10822 | [None][fix] Fix the potential access issue of cach... | hyukn | Checklist | +1/-2 | 23.5h |
| #10847 | [None][chore] Reduce tedious logs | chzblych | Checklist | +2/-2 | 1.2h |


---

## 三、卡点类型说明

| 卡点类型 | 说明 |
|---------|------|
| **Checklist** | PR Checklist未完成（开发者未勾选模板中的检查项） |
| **CI** | CI检查失败（包括单元测试、集成测试等） |
| **Title** | PR标题格式错误（不符合Conventional Commits规范） |
| **Review(Nx)** | Review要求修改N次 |
| **Precommit** | Pre-commit检查失败（代码格式问题） |

---

## 四、详细统计分析

### 4.1 直接合入PR的特征

- **平均合并时间**: 136.2 小时 (5.7 天)
- **平均代码变更**: +193/-85 lines
- **平均文件数**: 9.7 个文件

### 4.2 被阻塞PR的特征

- **平均合并时间**: 91.9 小时 (3.8 天)
- **平均代码变更**: +78/-63 lines
- **平均文件数**: 3.5 个文件

**最常见的卡点组合**:

| 组合 | 数量 | 占比 |
|------|------|------|
| Checklist | 56 | 64.4% |
| Review | 12 | 13.8% |
| Title | 9 | 10.3% |
| Checklist + Title | 7 | 8.0% |
| Precommit | 2 | 2.3% |


### 4.3 对比分析

| 指标 | 直接合入PR | 被阻塞PR | 差异 |
|------|-----------|---------|------|
| **平均合并时间** | 136.2h (5.7天) | 91.9h (3.8天) | -32.5% |
| **平均代码行数** | 278 | 141 | -49.2% |
| **平均文件数** | 9.7 | 3.5 | -63.7% |

---

## 五、关键发现

1. **直接合入率高达80.7%**，说明TensorRT-LLM项目的代码质量控制非常成熟。

2. **被阻塞PR的合并时间更短**：被阻塞PR平均需要3.8天，而直接合入PR只需5.7天。

3. **代码规模与阻塞的关系**：被阻塞PR的平均代码变更更小（141 vs 278 lines）。

4. **最常见的卡点组合是**: Checklist，占被阻塞PR的64.4%。

---

**报告生成**: 2026-01-22
**数据来源**: GitHub REST API
**分析工具**: Python
