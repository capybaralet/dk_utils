





from sklearn.datasets import fetch_mldata
data_set = fetch_mldata('yahoo-web-directory-topics')
train_set = (data_set['data'][:1000],data_set['target'][:1000])
validation_set = (data_set['data'][1000:],data_set['target'][1000:])
parameters = { 'C':{'min':0.01, 'max':1000.0,'type':'float'},
               'degree':{'min':1, 'max':5,'type':'integer'}}
outcome = {'name':'Classification accuracy'}
import whetlab
#access_token = '07beff82-6c3c-4eec-9e81-abeb7c0cda96'

scientist = whetlab.Experiment(name="Grammar Cells on blizzard lpcd",
                               description="Training Grammar Cells model on Blizzard Challenge 2013 dataset in Kyle Kastner's LPC representation.",
                               parameters=parameters,
                               outcome=outcome,
                               access_token=access_token)
job = scientist.suggest()
print job

from sklearn import svm
learner = svm.SVC(kernel='poly',**job)
learner.fit(*train_set)
accuracy = learner.score(*validation_set)
scientist.update(job,accuracy)
n_iterations = 1
for i in range(n_iterations):
    job = scientist.suggest()
    learner = svm.SVC(kernel='poly',**job)
    learner.fit(*train_set)
    accuracy = learner.score(*validation_set)
    scientist.update(job,accuracy)
best_job = scientist.best()
pendings = scientist.pending()
scientist.report()
scientist = whetlab.Experiment(name="Web page classifier",
                               access_token=access_token)

# ADD YOUR OWN JOB:
#job = {'C': 50.0, 'degree':1 }
#accuracy = 0.61320754717
#scientist.update(job,accuracy)

# CANCEL JOB:
#scientist.cancel(job)

# DELETING AN EXPERIMENT
#scientist.delete("Web page classifier", access_token);

