from pebl import config, data, prior

def fromconfig(data_=None, prior_=None):
    learnertype = pebl.config.get('learner.type')

    if ':' in learnertype:
        CustomLearner(
            data_ or data.fromconfig(), 
            prior_ or prior.fromconfig(),
            learnerurl=learnertype
        )
    else:
        learnermodule,learnerclass = learnertype.split('.')
        mymod = __import__("pebl.learner.%s" % learnermodule, fromlist=['pebl.learner'])

    mylearner = getattr(mymod, learnerclass)
    return mylearner(data_ or data.fromconfig(), prior_ or prior.fromconfig())

