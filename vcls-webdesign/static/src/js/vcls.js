odoo.define('vcls.DocumentsKanbanController', function(require) {
    "use strict";


    var KanbanRecord = require('documents.DocumentsKanbanRecord');
    var KanbanController = require('documents.DocumentsKanbanController');

    var VCLSDDocumentsKanbanController = KanbanController.include({

        custom_events: _.extend({}, KanbanController.prototype.custom_events, {
            kanban_reload: '_onKanbanReload',
        }),
        _onKanbanReload: function(e) {
            this.reload();
        },

    });


    var VCLSDDocumentsKanbanRecord = KanbanRecord.include({

        events: _.extend({}, KanbanRecord.prototype.events, {
            'click .vcls-generate': '_onGenerateCopyUrl',
            'click .vcls-copy': '_onCopyUrl',
        }),

        _onGenerateCopyUrl: function(e) {
            e.preventDefault();
            e.stopPropagation();
            var self = this;
            return self._rpc({
                    model: 'ir.attachment',
                    method: 'copy_url',
                    args: [$(e.target).data('id')],
                })
                .then(function(result) {
                    self.trigger_up('kanban_reload');
                    self._create_clipboard(result.url);
                });
        },
        _onCopyUrl: function(e) {
            var self = this;
            e.preventDefault();
            e.stopPropagation();
            this._create_clipboard(self.$el.find('.vcls-token').val());
        },

        _create_clipboard: function(val) {
            var $temp = $("<input>");
            $("body").append($temp);
            $temp.val(val).select();
            document.execCommand("copy");
            $temp.remove();
        }
    });

    return VCLSDDocumentsKanbanRecord, VCLSDDocumentsKanbanController;

});
