    # try:

    # # get all models (possibly add filter to singular model?)
    #   models = sdk.all_lookml_models() # returns lookmlModel objects

    #   for model in models:
    #         print(f"Model: {model.name}")
    #         explores = model.explores  # list of explores in the model object
    #         for explore in explores:
    #             print(f" - Explore: {explore.name}")
    #             explore_details = sdk.lookml_model_explore( # returns LookmlModelExplore objects
    #                 lookml_model_name=model.name,
    #                 explore_name=explore.name,
    #                 fields="fields" # fields --> LookmlModelExploreFieldSet
    #             )

    #             all_fields = []

    #             if explore_details.fields and explore_details.fields.dimensions:
    #                     for dimension in explore_details.fields.dimensions:
    #                         field_def = {
    #                             "view_name": dimension.view_label,
    #                             "field_name": dimension.label_short,
    #                             "type": "Dimension",  # Indicating it's a dimension
    #                             "sql": dimension.sql,
    #                         }
    #                         all_fields.append(field_def)

    #             if explore_details.fields and explore_details.fields.measures:
    #                     for measure in explore_details.fields.measures:
    #                         field_def = {
    #                             "view_name": measure.view_label,
    #                             "field_name": measure.label_short,
    #                             "type": "Measure",  # Indicating it's a measure
    #                             "sql": measure.sql,
    #                         }
    #                         all_fields.append(field_def)

    #                 # Print all fields
    #             print("    All Fields:")
    #             for field in all_fields:
    #                 print(f"      - {field['view_name']}.{field['field_name']} (Type: {field['type']})")

    # except Exception as e:
    #     print(f"An error occurred: {e}")
