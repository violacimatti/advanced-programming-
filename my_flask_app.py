from flask import Flask, render_template, request
import pandas as pd 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  
    
@app.route('/basic_info')
def basic_info():
    info = reader.get_basic_info()
    return render_template('basic_info.html', info=info)

@app.route('/unique_seqids')
def unique_seqids():
    seqids = reader.unique_seqids()
    return render_template('unique_seqids.html', seqids=seqids)

@app.route('/unique_types')
def unique_types():
    types = reader.unique_types()
    return render_template('unique_types.html', types=types)

@app.route('/features_by_source')
def features_by_source():
    features_count = reader.count_features_by_source()
    return render_template('features_by_source.html', features_count=features_count)

@app.route('/entries_by_type')
def entries_by_type():
    entries_count = reader.count_entries_by_type()
    return render_template('entries_by_type.html', entries_count=entries_count)

@app.route('/entire_chromosomes')
def entire_chromosomes():
    new_dataset = reader.filter_entire_chromosomes()
    return render_template('entire_chromosomes.html', new_dataset=new_dataset)

@app.route('/unassembled_sequences')
def unassembled_sequences():
    fraction_unassembled = reader.unassembled_sequences()
    return render_template('unassembled_sequences.html', fraction_unassembled=fraction_unassembled)

@app.route('/ensembl_havana')
def ensembl_havana():
    ensembl_havana_data = reader.filter_ensembl_havana()
    return render_template('ensembl_havana.html', ensembl_havana_data=ensembl_havana_data)

@app.route('/entries_by_type_ensembl_havana')
def entries_by_type_ensembl_havana():
    entries_count_ensembl_havana = reader.count_entries_by_type_ensembl_havana()
    return render_template('entries_by_type_ensembl_havana.html', entries_count_ensembl_havana=entries_count_ensembl_havana)

@app.route('/gene_names_ensembl_havana')
def gene_names_ensembl_havana():
    gene_names = reader.get_gene_names_ensembl_havana()
    return render_template('gene_names_ensembl_havana.html', gene_names=gene_names)

if __name__=='__main__':
	app.run(debug=True)
	




