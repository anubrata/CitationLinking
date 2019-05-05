## This code is from the issue opened in the OpneNMT-py repo
## URL : https://github.com/OpenNMT/OpenNMT-py/issues/575

import sys
sys.path.append("/work/05773/anubrata/maverick2/OpenNMT-py")

import onmt
import onmt.inputters
import onmt.translate
import onmt.model_builder
from collections import namedtuple

# Load the model.
Opt = namedtuple('Opt', ['model', 'data_type', 'reuse_copy_attn', "gpu"])

opt = Opt("/work/05773/anubrata/maverick2/CitationLinking/models/scisumm_step_10000.pt", "text",False, 0)
fields, model, model_opt =  onmt.model_builder.load_test_model(opt,{"reuse_copy_attn":False})

# Test data
# data = onmt.inputters.build_dataset(fields, "text", None, use_filter_pred=False, src_path='./val.txt')
data_iter = onmt.inputters.OrderedIterator(
        dataset="/work/05773/anubrata/maverick2/CitationLinking/preprocessed/scisumm.valid.0.pt", device='cuda',
        batch_size=1, train=False, sort=False,
        sort_within_batch=True, shuffle=False)

# Translator
translator = onmt.translate.Translator(model, fields,
                                           beam_size=5,
                                           n_best=1,
                                           global_scorer=onmt.translate.GNMTGlobalScorer(0, 0, "none", "none"),
                                           gpu=True)

builder = onmt.translate.TranslationBuilder(
        data, translator.fields,
        1, False, None)

for j, batch in enumerate(data_iter):
        batch_data = translator.translate_batch(batch, data)
        translations = builder.from_batch(batch_data)
        print("src:", " ".join(translations[0].src_raw))
        print("tgt:", " ".join(translations[0].pred_sents[0]))
        print("idx:",str(j))
        print("-----")


