import scanpy as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
adata.var_names_make_unique()
sc.pp.recipe_zheng17(adata)
sc.pp.pca(adata)
sc.pp.neighbors(adata)
# sc.pl.pca(adata, na_color="blue", save="unfiltered.png")
sc.tl.leiden(adata)
# new_cluster_names = [
#     'aECvar1', 'vECvar1',
#     'FB1', 'PCvar1',
#     'ACvar1', 'ACvar2',
#     'OLvar1', 'OLvar2',
#     'FB2var1', 'aECvar2',
#     'EC2var1', 'aaSMC',
#     'ACvar3', 'OLvar3',
#     'unknown-1', 'unknown-2',
#     'FB2var2', 'EC2var2',
#     'OLvar4', 'vECvar2',
#     'OLvar5', 'ACvar4',
#     'PCvar2', 'MGvar1',
#     'vECvar3', 'MGvar2',
#     'unknown-3']
# adata.rename_categories('leiden', new_cluster_names)
sc.pl.dotplot(adata, var_names='leiden', gene_symbols='gene_ids')
# ['Tsc22d1', 'Eomes', 'Igfbp3', 'Adarb2', 'Bcl11b', 'Tnni3']
# sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
# sc.pl.rank_genes_groups(adata, save=True)
# sc.tl.umap(adata, maxiter=1000)
# sc.pl.umap(adata, color=['leiden'], save="UMAP.png")
# sc.tl.tsne(adata)
# sc.pl.tsne(adata, color='leiden', legend_loc='on data', title='', frameon=False, save="labeled_tSNE.png")

